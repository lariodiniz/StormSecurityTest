# coding: utf-8

#--------------//////////----------------------

#Projeto Criado por: Lário Diniz
#Contatos: developer.lario@gmail.com

#--------------//////////----------------------

from django import forms


class OrdeneForm(forms.Form):
    "Formulario que Ordena Filmes"
    choices = [(0, 'Ordenar por'), (1, 'a - z'), (2, 'z - a')]
    order = forms.ChoiceField(label='', choices=choices,
                           widget=forms.Select(attrs={'onchange':'this.form.submit()'}))