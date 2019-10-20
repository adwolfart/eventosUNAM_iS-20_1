from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from Eventos.models import Evento, Direccion, Etiquetas
from Eventos.forms import EventoForm,DireccionForm,EtiquetasForm
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return HttpResponse("Index")


class EventoList(ListView):
    """
    Clase que representa una lista de eventos
    ...

    Atributos
    ----------
    model: 
        indica el modelo al que hace referencia la lista
    template_name: str
        nombre del template con la vista de la lista
    """

    template_name = 'Eventos/evento_lista.html'

    def get_queryset(self):
        return Evento.objects.all().order_by('pk')

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        if 'evento' not in context:
            context['evento'] = Evento.objects.all().order_by('pk')
        if 'direccion' not in context:
            context['direccion'] = Direccion.objects.all().order_by('evento')
        return context   



class EventoCreate(CreateView):
    """
    Clase que representa la creacion de un evento
    ...

    Atributos
    ----------
    model: 
        indica el modelo al que hace referencia la lista
    template_name: str
        nombre del template con la vista de la lista
    """
    model = Evento
    form_class = EventoForm
    dir_form = DireccionForm
    etiq_form = EtiquetasForm
    template_name = 'Eventos/eventosform.html'
    success_url = reverse_lazy('evento_lista')


    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        direccion_f = self.dir_form(initial=self.initial)
        context = {
            'form': EventoForm(),
            'direccion': DireccionForm(),
            'etiquetas': EtiquetasForm(),
        }
        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        direccion_f = self.dir_form(request.POST)
        e_f = self.etiq_form(request.POST)
        if form.is_valid() and direccion_f.is_valid() and e_f.is_valid():
            eventon = form.save()
            direccion = direccion_f.save(commit=False)
            direccion.evento = eventon
            direccion.save()
            etiqueta = e_f.save(commit=False)
            lista_de_etiquetas = str(etiqueta.lista).split(",")
            for e in lista_de_etiquetas:
                etiqueta.lista = e
                etiqueta.evento = eventon
                etiqueta.save()
            return redirect('Eventos:listaEvento')
        context = {
        'form': form,
        'direccion': direccion_f,
        }
        return render(request, self.template_name, context)


class EventoUpdate(UpdateView):
    """
    Clase que representa la edicion y actualizacion de un evento
    ...

    Atributos
    ----------
    model: 
        indica el modelo al que hace referencia la lista
    template_name: str
        nombre del template con la vista de la lista
    model = Evento
    form_class = EventoForm
    template_name = 'Eventos/eventosform.html'
    success_url = reverse_lazy('evento_lista')
    """
    model = Evento
    form_class = EventoForm
    dir_form = DireccionForm
    template_name = 'Eventos/eventosform.html'
    success_url = reverse_lazy('evento_lista')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        if 'evento' not in context:
            context['evento'] = self.form_class()
        if 'direccion' not in context:
            context['direccion'] = self.dir_form()
        return context





class EventoDelete(DeleteView):
    """
    Clase que representa la eliminacion de un evento
    ...

    Atributos
    ----------
    model: 
        indica el modelo al que hace referencia la lista
    template_name: str
        nombre del template con la vista de la lista
    """
    model = Evento
    template_name = 'Eventos/evento_delete.html'
    success_url = reverse_lazy('evento_lista')


