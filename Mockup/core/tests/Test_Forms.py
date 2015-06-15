# coding: utf-8

#--------------//////////----------------------

#Projeto Criado por: Lário Diniz
#Contatos: developer.lario@gmail.com

#--------------//////////----------------------

from django.test import TestCase
from Mockup.core.forms import OrdeneForm

class TestOrdeneForm(TestCase):
    "Testa o Form de Organizar"
    def test_has_form(self):
        'Verifica se as escolhas estão corretas'
        form=OrdeneForm()
        self.assertItemsEqual([(0, 'Ordenar por'), (1, 'a - z'), (2, 'z - a')], form.choices)