from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Fornecedor
from .forms import FornecedorForm

class ListaFornecedorView(ListView):
    model = Fornecedor

class FornecedorCreateView(CreateView):
    model = Fornecedor
    form_class = FornecedorForm
    success_url = '/fornecedores/'

class FornecedorUpdateView(UpdateView):
    model = Fornecedor
    form_class = FornecedorForm
    success_url = '/fornecedores/'

class FornecedorDeleteView(DeleteView):
    model = Fornecedor
    success_url = '/fornecedores/'
