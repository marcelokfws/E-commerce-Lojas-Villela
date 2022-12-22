from django.shortcuts import render,redirect
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse
from django.contrib import messages

class SalvarPedido(View):
    template_name = 'pedido/pagar.html'

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.error(
                self.request,
                'Você precisa fazer login.'
            )
            return redirect('perfil:criar')
        
        contexto = {
            
        }

        return render(self.request,self.template_name, contexto)

class Pagar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Fechar Pedido')

class Detalhe(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhe')
