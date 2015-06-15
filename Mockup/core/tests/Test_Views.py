# coding: utf-8

#--------------//////////----------------------

#Projeto Criado por: Lário Diniz
#Contatos: developer.lario@gmail.com

#--------------//////////----------------------

from django.test import TestCase


class TestHomepage(TestCase):
    "Teste da View Homepage"

    def setUp(self):
        self.resp=self.client.get("/")

    def test_get(self):
        'Verifica se o staus code é 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'verifica qual template esta sendo usado'
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_html(self):
        'Verifica o HTML'
        self.assertContains(self.resp, '<form id="ordenar"')

class genero_detail(TestCase):
    "Teste da View genero_detail"

    def setUp(self):
        self.resp=self.client.get("/")

    def test_get(self):
        'Verifica se o staus code é 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'verifica qual template esta sendo usado'
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_html(self):
        'Verifica o HTML'
        self.assertContains(self.resp, '<form id="ordenar"')