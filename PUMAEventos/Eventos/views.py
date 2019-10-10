from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

class About(View):
    template = 'Evento/eventoform.html'
    context = {'title': 'Crea Evento'}

    def get(self, request):
        return render(request, self.template, self.context)
