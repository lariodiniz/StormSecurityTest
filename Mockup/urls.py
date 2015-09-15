# coding: utf-8

#--------------//////////----------------------

#Projeto Criado por: Lário Diniz
#Contatos: developer.lario@gmail.com

#--------------//////////----------------------


from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from Mockup.core.views import Homepage, Moviedetail, Atordetail, Genresdetail

urlpatterns = patterns('',
                       url(r'^media/(.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
                        url(r'^$', Homepage.as_view(), name='homepage'),
                        url(r'^filme/(?P<slug>[\w_-]+)$', Moviedetail.as_view(), name='movie_detail'),
                        url(r'^(?P<slug>[\w_-]+)$', Genresdetail.as_view(), name='genre_detail'),
                        url(r'^actor/(?P<slug>[\w_-]+)$', Atordetail.as_view(), name='actor_detail'),
                        #url(r'^grappelli/', include('grappelli.urls')),
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

