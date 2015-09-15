# coding: utf-8

#--------------//////////----------------------

#Projeto Criado por: Lário Diniz
#Contatos: developer.lario@gmail.com

#--------------//////////----------------------

from django.shortcuts import render, get_object_or_404


from Mockup.core.models import Movies, Genres, Actors
from Mockup.core.forms import OrdeneForm

from django.views.generic import ListView,DetailView


class Homepage(ListView):
    model = Movies
    template_name = 'core/index.html'



class Moviedetail(DetailView):
    template_name = 'core/interna.html'
    model = Movies

    def get_context_data(self, **kwargs):
        context = super(Moviedetail, self).get_context_data(**kwargs)
        movies= super(Moviedetail, self).get_object()
        generos = movies.genres.all()

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
        context['relacionados']=relacionados
        return context

class Atordetail(DetailView):
    model = Actors
    template_name = 'core/artista.html'

    def get_context_data(self, **kwargs):
        context = super(Atordetail, self).get_context_data(**kwargs)
        actor= super(Atordetail, self).get_object()
        movies = Movies.objects.filter(actors=actor)
        context['relacionados']=movies
        return context

class Genresdetail(DetailView):
    model=Genres
    template_name = 'core/genero.html'

    def get_context_data(self, **kwargs):
        context = super(Genresdetail, self).get_context_data(**kwargs)
        genre= super(Genresdetail, self).get_object()
        context['movies']=Movies.objects.filter(genres=genre)
        return context



