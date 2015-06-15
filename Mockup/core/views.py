# coding: utf-8

#--------------//////////----------------------

#Projeto Criado por: Lário Diniz
#Contatos: developer.lario@gmail.com

#--------------//////////----------------------

from django.shortcuts import render, get_object_or_404


from Mockup.core.models import Movies, Genres, Actors
from Mockup.core.forms import OrdeneForm

def newpage(request, template, context):
    return render(request, template, context)

def createpage(request, template, context, movies):
    print "AQUI"
    print request.POST
    if request.POST['order'] == '1':
        context['movies']=movies.order_by('name')
    elif request.POST['order'] == '2':
        context['movies']=movies.order_by('-name')

    return render(request, template, context)

def homepage(request):
    movies=Movies.objects.all()
    context = {'movies':movies, 'form':OrdeneForm()}
    template='index.html'
    if request.method == 'POST':
        print "homepage"
        return createpage(request, template, context, movies)
    else:
        return newpage(request, template, context)

def genres_detail(request, slug):
    generos=Genres.objects.get(slug=slug)
    template='genero.html'
    movies=Movies.objects.filter(genres=generos)
    context = {'movies': movies, "generos":generos, 'form':OrdeneForm()}
    if request.method == 'POST':
        return createpage(request,template, context, movies)
    else:
        return newpage(request, template, context)


def actor_detail(request, slug):
    ator=Actors.objects.get(slug=slug)
    relacionados=Movies.objects.filter(actors=ator)
    if len(relacionados)>20:
        relacionados=relacionados[0:20]

    context = {'ator':ator, 'relacionados':relacionados}

    return render(request, 'artista.html', context)



def movie_detail(request, slug):

    SLUG = get_object_or_404(Movies, slug=slug)
    movies = Movies.objects.get(slug=slug)
    generos = movies.genres.all()
    print generos
    atores =  movies.actors.all()
    comum_generos = Movies.objects.filter(genres=generos)
    comum_atores = Movies.objects.filter(actors=atores)
    re={}
    for x in comum_generos:
        if movies.name != x.name:
            if re.has_key(x.name):
                re[x.name][0]+=1
            else:
                re[x.name]=[1,x]

    for x in comum_atores:
        if movies.name != x.name:
            if re.has_key(x.name):
                re[x.name][0]+=1
            else:
                re[x.name]=[1,x]

    relacionados=[]
    for x in re:
        relacionados.append(re[x][1])

    if len(relacionados)>10:
        relacionados=relacionados[0:10]

    context = {'movie': movies , 'generos': generos, 'atores': atores, 'relacionados':relacionados,'slug': SLUG }
    return render(request, 'interna.html', context)