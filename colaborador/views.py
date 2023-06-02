from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Colaborador
from .forms import ColaboradorForm

class ListaColaboradorView(ListView):
    model = Colaborador

class ColaboradorCreateView(CreateView):
    model = Colaborador
    form_class = ColaboradorForm
    success_url = '/colaboradores/'

class ColaboradorUpdateView(UpdateView):
    model = Colaborador
    form_class = ColaboradorForm
    success_url = '/colaboradores/'

class ColaboradorDeleteView(DeleteView):
    model = Colaborador
    success_url = '/colaboradores/'
