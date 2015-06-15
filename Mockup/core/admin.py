# coding: utf-8

#--------------//////////----------------------

#Projeto Criado por: Lário Diniz
#Contatos: developer.lario@gmail.com

#--------------//////////----------------------

from django.contrib import admin
from Mockup.core.models import Movies, Actors, Genres

class MoviesAdmin(admin.ModelAdmin):
    list_display = ('name','synopsis', 'slug', 'img')

class ActorsAdmin(admin.ModelAdmin):
    list_display = ('name','description')

class GenresAdmin(admin.ModelAdmin):
    list_display = ('type','description')

admin.site.register(Movies, MoviesAdmin)
admin.site.register(Actors, ActorsAdmin)
admin.site.register(Genres, GenresAdmin)
