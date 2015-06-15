# coding: utf-8

#--------------//////////----------------------

#Projeto Criado por: Lário Diniz
#Contatos: developer.lario@gmail.com

#--------------//////////----------------------

from django.test import TestCase
from Mockup.core.models import Actors,Genres, Movies


class TestActors(TestCase):
    "Testa o Model Actors"

    def setUp(self):
        self.obj=Actors(name='Graham Arthur Chapman',
                        slug='graham-arthur-chapman',
                        parents='Reino unido',
                        description='Graham Arthur Chapman foi um actor e escritor britânico e membro do grupo Monty Python.',
                        img='graham-arthur-chapman',
                        )
    def test_create(self):
        self.obj.save()
        self.assertEqual(1, self.obj.id)

class TestGenres(TestCase):
    "Testa o Model Genres"

    def setUp(self):
        self.obj=Genres(type='Comedia',
                        slug= 'comedia',
                        description='A comédia é o uso de humor nas artes cênicas.'
                        )
    def test_create(self):
        self.obj.save()
        self.assertEqual(1, self.obj.id)

class TestMovies(TestCase):
    "Testa o Model movies"

    def setUp(self):
        self.obj=Movies(name='Monty Python - Em Busca do Cálice Sagrado',
                        original_name='Monty Python and the Holy Grail',
                        slug='monty-python-and-the-holy-grail',
                        synopsis='Monty Python - Em Busca do Cálice Sagrado é um filme de comédia britânico de 1975.',
                        img='cartaz666',
                        )
    def test_create(self):
        self.obj.save()
        self.assertEqual(1, self.obj.id)



