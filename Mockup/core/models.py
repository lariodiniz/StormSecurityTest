# coding: utf-8

#--------------//////////----------------------

#Projeto Criado por: Lário Diniz
#Contatos: developer.lario@gmail.com

#--------------//////////----------------------


from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from django.db.models import signals
from django.template.defaultfilters import slugify


class Actors(models.Model):
    "Modelo da tabela de Atores"
    name=models.CharField(_('Nome'), max_length=250)
    slug= models.SlugField(_('Slug'), blank=True, unique=True)
    parents=models.CharField(_('Pais'), max_length=250)
    description=models.TextField(_(u'Descrição'), blank=True)
    img=models.CharField(_('img'), max_length=250, blank=True)

    class Meta:
        verbose_name = _('Ator')
        verbose_name_plural = _('Atores')
        #ordering = ['name']

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Mockup.core.views.actor_detail', kwargs={'slug': self.slug})

class Genres(models.Model):
    "Modelo da tabela Generos"
    type=models.CharField(_('Tipo'), max_length=250)
    slug= models.SlugField(_('Slug'), blank=True, unique=True)
    description=models.TextField(_(u'Descrição'), blank=True)

    class Meta:
        verbose_name = _('Genero')
        verbose_name_plural = _('Generos')
        #ordering = ['tipo']

    def __unicode__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('Mockup.core.views.genres_detail', kwargs={'slug': self.slug})

class Movies(models.Model):
    "Modelo da tabela de Filmes"

    name=models.CharField(_('Nome'), max_length=250)
    original_name=models.CharField(_('Nome Original'), max_length=250, blank=True)
    slug= models.SlugField(_('Slug'), blank=True, unique=True)
    synopsis=models.TextField(_(u'Sinopse'), blank=True)
    img=models.CharField(_('img'), max_length=250, blank=True)
    actors=models.ManyToManyField('Actors', verbose_name=_('Atores'), blank=True)
    genres=models.ManyToManyField('Genres', verbose_name=_('Genero'), blank=True)


    class Meta:
        verbose_name = _('Filme')
        verbose_name_plural = _('Filmes')
        #ordering = ['name']


    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Mockup.core.views.movie_detail', kwargs={'slug': self.slug})
    
# ---------- Funções ------------#
def Movie_pre_save(signal, instance, sender, **kwargs):

    """Este signal gera um slug automaticamente. Ele verifica se ja existe um
    artigo com o mesmo slug e acrescenta um numero ao final para evitar
    duplicidade
    """
    if not instance.slug:
        slug = slugify(instance.original_name)
        new_slug = slug
        counter = 0
        while sender.objects.filter(slug=new_slug).exclude(id=instance.id).count() > 0:
            counter += 1
            new_slug = '%s-%d'%(slug, counter)

        instance.slug = new_slug

def Actor_pre_save(signal, instance, sender, **kwargs):
    """Este signal gera um slug automaticamente. Ele verifica se ja existe um
    artigo com o mesmo slug e acrescenta um numero ao final para evitar
    duplicidade
    """
    if not instance.slug:
        slug = slugify(instance.name)
        novo_slug = slug
        contador = 0
        while sender.objects.filter(slug=novo_slug).exclude(id=instance.id).count() > 0:
            contador += 1
            novo_slug = '%s-%d'%(slug, contador)

        instance.slug = novo_slug


def Genere_pre_save(signal, instance, sender, **kwargs):
    """Este signal gera um slug automaticamente. Ele verifica se ja existe um
    artigo com o mesmo slug e acrescenta um numero ao final para evitar
    duplicidade
    """

    if not instance.slug:
        slug = slugify(instance.type)
        novo_slug = slug
        contador = 0
        while sender.objects.filter(slug=novo_slug).exclude(id=instance.id).count() > 0:
            contador += 1
            novo_slug = '%s-%d'%(slug, contador)

        instance.slug = novo_slug


signals.pre_save.connect(Movie_pre_save, sender=Movies)
signals.pre_save.connect(Actor_pre_save, sender=Actors)
signals.pre_save.connect(Genere_pre_save, sender=Genres)


