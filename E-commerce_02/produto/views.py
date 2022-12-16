from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from . import models

class ListaProduto(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 10

class DetalheProduto(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhe produto')

class AdicionarAoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Adicionar ao Carrinho')

class RemoverDoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse(' Remover do Carrinho')

class Carrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Carrinho')

class Finalizar(View):
    pass
