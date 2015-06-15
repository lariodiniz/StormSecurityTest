# coding: utf-8

#--------------//////////----------------------

#Projeto Criado por: Lário Diniz
#Contatos: developer.lario@gmail.com

#--------------//////////----------------------


from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
                       url(r'^media/(.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
                        url(r'^$','Mockup.core.views.homepage', name='homepage'),
                        url(r'^filme/(?P<slug>[\w_-]+)$', 'Mockup.core.views.movie_detail', name='movie_detail'),
                        url(r'^(?P<slug>[\w_-]+)$', 'Mockup.core.views.genres_detail', name='genre_detail'),
                        url(r'^actor/(?P<slug>[\w_-]+)$', 'Mockup.core.views.actor_detail', name='actor_detail'),
                        url(r'^grappelli/', include('grappelli.urls')),
                        url(r'^admin/', include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'ssmockup.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
)

#--------------//////////----------------------
# Configuração para o Heroku Comentar esta parte caso nescessite usar local.
#--------------//////////----------------------

urlpatterns += patterns('django.views.static',
                        url(r'^static/(?P<path>.*)$','serve',{'document_root': settings.STATIC_ROOT}),
                        )

