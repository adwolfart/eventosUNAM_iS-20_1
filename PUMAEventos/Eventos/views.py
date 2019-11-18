from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from Eventos.models import Evento, RegEvento, AsigStaff
from Eventos.forms import EventoForm, DelEventoForm, UpdateForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail


from django.template import loader
import qrcode


def index(request):
    return HttpResponse("Index")

class OnePost(View):
    """
        Displays just one post
    """
    template = 'Eventos/updateEvento.html'
    context = {}

    def get(self, request, post_id):
        """
            GET in one post
        """
        post = Evento.objects.get(id=post_id)
        #post = get_object_or_404(Post, id=post_id)
        self.context['post'] = post

        self.context['title'] = str(post)

        return render(request, self.template, self.context)


    def post(self, request, post_id):
        """
            Validates and do the login
        """
        form = UpdateForm(request.POST)
        print(form)


        if form.is_valid():
            try:
                u = Evento.objects.get(id = form.cleaned_data['id'])
                correo = request.POST.get('correo', '')

                if(u.correo == correo):
                    titulo = request.POST.get('titulo', '')
                    fecha_de_inicio = request.POST.get('fecha_de_inicio','')
                    hora_de_inicio = request.POST.get('hora_de_inicio','')
                    fecha_final = request.POST.get('fecha_final','')
                    hora_final = request.POST.get('hora_final','')
                    cupo_maximo = request.POST.get('cupo_maximo','')
                    descripcion = request.POST.get('descripcion','')
                    ubicacion = request.POST.get('ubicacion','')
                    entidad = request.POST.get('entidad','')
                    etiqueta1 = request.POST.get('etiqueta1','')
                    etiqueta2 = request.POST.get('etiqueta2','')
                    etiqueta3 =  request.POST.get('etiqueta3','') 

                    u.titulo = titulo
                    u.fecha_de_inicio = fecha_de_inicio
                    u.hora_de_inicio = hora_de_inicio
                    u.fecha_final = fecha_final
                    u.hora_final = hora_final
                    u.cupo_maximo = cupo_maximo
                    u.descripcion = descripcion
                    u.ubicacion = ubicacion
                    u.entidad = entidad
                    u.etiqueta1 = etiqueta1
                    u.etiqueta2 = etiqueta2
                    u.etiqueta3 = etiqueta3
                    u.save()                  
                    print("actualizado")
                else:
                    print("No puedes eliminar este evento, no te pertenece")
                
            except:
                print("no existe o error") 

        self.context['form'] = form

        return redirect("Eventos:listaEventos")
        #return render(request, self.template, self.context)


class EventoList(ListView):
    """
        Index in my Web Page but with Clased based views.
    """
    template = 'Eventos/verEventos.html'
    context = {'title': 'Index'}

    #def get(self, request):

        #all_posts = Post.objects.all()
        #self.context['posts'] = all_posts
    def get(self, request):
        """
            Get in my Index.
        """
        all_posts = Evento.objects.all()
        self.context['posts'] = all_posts
        return render(request, self.template, self.context)


    def post(self, request):
        """
            Validates and do the login
        """
        form = EventoForm(request.POST)
        print(form)
        if form.is_valid():
            print("creado")                  


        self.context['form'] = form

        return redirect("Home:home")
        #return render(request, self.template, self.context) 



class EventoCreate(CreateView):
    """
        Index in my Web Page but with Clased based views.
    """
    template = 'Eventos/crearEvento.html'
    context = {'title': 'Index'}

    def get(self, request):
        """
            Get in my Index.
        """
        #all_posts = Post.objects.all()
        #self.context['posts'] = all_posts
        return render(request, self.template, self.context)


    def post(self, request):
        """
            Validates and do the login
        """
        form = EventoForm(request.POST)
        print(form)
        if form.is_valid():
            titulo = request.POST.get('titulo', '')
            fecha_de_inicio = request.POST.get('fecha_de_inicio','')
            hora_de_inicio = request.POST.get('hora_de_inicio','')
            fecha_final = request.POST.get('fecha_final','')
            hora_final = request.POST.get('hora_final','')
            cupo_maximo = request.POST.get('cupo_maximo','')
            descripcion = request.POST.get('descripcion','')
            ubicacion = request.POST.get('ubicacion','')
            entidad = request.POST.get('entidad','')
            correo = request.POST.get('correo','')
            etiquetas = request.POST.get('etiquetas','')

            u = Evento.objects.create(titulo = titulo, 
                                    fecha_de_inicio = fecha_de_inicio,
                                    cupo_maximo = cupo_maximo,
                                    descripcion = descripcion,
                                    ubicacion = ubicacion,
                                    correo = correo)

            try:
                u.entidad = entidad
                u.save()
            except:
                print("entidad invalida")

            try:               
                u.etiquetas = etiquetas
                u.save()
            except:
                print("etiquetas invalida")                                    

            try:
                u.hora_de_inicio = hora_de_inicio
                u.save()
            except:
                print("hora de inicio invalida")


            try:
                u.fecha_final = fecha_final
                u.save()
            except:
                print("fecha final invalida")

            try:
                u.hora_final = hora_final
                u.save()
            except:
                print("hora final invalida")


                           

        self.context['form'] = form

        return redirect("Eventos:listaEventos")
        #return render(request, self.template, self.context)




class EventoUpdate(View):
    """
        Index in my Web Page but with Clased based views.
    """
    template = 'Eventos/verEventosInscritos.html'
    context = {'title': 'Index'}

    def get(self, request, post_id, user_mail):
        """
            Get in my Index.
        """
        #all_posts = Post.objects.all()
        #self.context['posts'] = all_posts
        all_posts = Evento.objects.all()
        self.context['posts'] = all_posts
        all_events = RegEvento.objects.all()
        self.context['eventos'] = all_events

        try:
            post = Evento.objects.get(id=post_id)
            count = 0
            for i in all_events:
                if(i.id_Evento == post_id):
                    count+=1
            if(count< post.cupo_maximo):
                RegEvento.objects.create(id_Evento = post_id, email_Usuario = user_mail)        
                img = qrcode.make(str(user_mail) + '$' + str(post_id))                
                img.save('Eventos/static/Eventos/img/'+ str(user_mail) + '$' + str(post_id) + '.png')
                html_message = loader.render_to_string(
                    'Eventos/invitacion.html',
                    {
                        'user_mail': user_mail,
                        'post_id':  post_id,
                        
                    }
                )
                send_mail(
                    'Inscripción a Evento',
                    'Te acabas de registrar a un evento',
                    'pumaeventosunam@gmail.com',
                    [user_mail],
                    fail_silently=False,
                    html_message = html_message,
                    ) 
                print("Exito en el registro")
            else:
                print("Ya no hay cupo")
        except Exception as e: print(e)




        return render(request, self.template, self.context)





        
class EventoDelete(View):
    """
        Index in my Web Page but with Clased based views.
    """
    template = 'Eventos/borrarEvento.html'
    context = {'title': 'Index'}

    def get(self, request):
        """
            Get in my Index.
        """
        #all_posts = Post.objects.all()
        #self.context['posts'] = all_posts
        return render(request, self.template, self.context)



    def post(self, request):
        """
            Validates and do the login
        """
        form = DelEventoForm(request.POST)
        if form.is_valid():
            try:
                u = Evento.objects.get(id = form.cleaned_data['id'])
                correo = request.POST.get('correo', '')

                v = RegEvento.objects.all()
                                    

                if(u.correo == correo):
                    for i in v:
                        if(i.id_Evento == u.id):
                            print("eliminado")
                            print(i.id_Evento)
                            print("aoeu")
                            print(u.id)
                            send_mail(
                            'Cancelacion Evento',
                            'Da click para confirmar tu registro',
                            'pumaeventosunam@gmail.com',
                            [i.email_Usuario],
                            fail_silently=False,
                            )  
                else:
                    print("No puedes eliminar este evento, no te pertenece")
                
            except:
                print("no existe") 

        return redirect("Eventos:listaEventos")
        #return render(request, self.template, self.context)



class TwoPost(View):
    """
        Displays just one post
    """
    template = 'Eventos/detallesEvento.html'
    context = {}

    def get(self, request, post_id):
        """
            GET in one post
        """
        post = Evento.objects.get(id=post_id)
        #post = get_object_or_404(Post, id=post_id)
        self.context['post'] = post

        self.context['title'] = str(post)

        return render(request, self.template, self.context)


    def post(self, request, post_id):
        """
            Validates and do the login
        """
        form = UpdateForm(request.POST)
        print(form)


        if form.is_valid():
            try:
                u = Evento.objects.get(id = form.cleaned_data['id'])
                correo = request.POST.get('correo', '')

                if(u.correo == correo):
                    titulo = request.POST.get('titulo', '')
                    fecha_de_inicio = request.POST.get('fecha_de_inicio','')
                    hora_de_inicio = request.POST.get('hora_de_inicio','')
                    fecha_final = request.POST.get('fecha_final','')
                    hora_final = request.POST.get('hora_final','')
                    cupo_maximo = request.POST.get('cupo_maximo','')
                    descripcion = request.POST.get('descripcion','')
                    ubicacion = request.POST.get('ubicacion','')
                    entidad = request.POST.get('entidad','')
                    etiqueta1 = request.POST.get('etiqueta1','')
                    etiqueta2 = request.POST.get('etiqueta2','')
                    etiqueta3 =  request.POST.get('etiqueta3','') 

                    u.titulo = titulo
                    u.fecha_de_inicio = fecha_de_inicio
                    u.hora_de_inicio = hora_de_inicio
                    u.fecha_final = fecha_final
                    u.hora_final = hora_final
                    u.cupo_maximo = cupo_maximo
                    u.descripcion = descripcion
                    u.ubicacion = ubicacion
                    u.entidad = entidad
                    u.etiqueta1 = etiqueta1
                    u.etiqueta2 = etiqueta2
                    u.etiqueta3 = etiqueta3
                    u.save()                  
                    print("actualizado")
                else:
                    print("No puedes eliminar este evento, no te pertenece")
                
            except:
                print("no existe o error") 

        self.context['form'] = form

        return redirect("Eventos:listaEventos")
        #return render(request, self.template, self.context)


class AsignarStaff(View):
    """
        Displays just one post
    """
    template = 'Eventos/asigStaff.html'
    context = {}


    def post(self, request):
        """
            Validates and do the login
        """

        try:
            eventoid = request.POST.get('id', '')
            correo = request.POST.get('correo', '')
            AsigStaff.objects.create(id_Evento = eventoid, email_staff = correo)
            print("Exito en la asignación de staff")
        except:
            print("Error en la asignacion de staff")

        
        return render(request, self.template, self.context)
        #return render(request, self.template, self.context)



class Etiquetas(View):
    """
        Displays just one post
    """
    template = 'Eventos/verEventos.html'
    context = {}


    def post(self, request):
        """
            Validates and do the login
        """

        try:
            eventoid = request.POST.get('id', '')
            etiquetas = request.POST.get('etiquetas', '')
            u = Evento.objects.get(id=eventoid)

            u.etiquetas = etiquetas
            u.save()
            print("Exito en la actualizacion de etiquetas")
        except:
            print("Error en la actualizacion")

        
        return redirect("Eventos:listaEventos")
        #return render(request, self.template, self.context)



class Buscar(View):
    """
        Displays just one post
    """
    template = 'Eventos/busqueda.html'
    context = {}


    def post(self, request):
        """
            Validates and do the login
        """

        try:
            busqueda = request.POST.get('busqueda', '')
            u = Evento.objects.all()

            ids = []
            for i in u:
                
                tmp = str(i.titulo) + str(i.descripcion) + str(i.etiquetas)
                if( busqueda in tmp):
                    print("True")
                    ids.append(i.id)
            print(ids)

            u = Evento.objects.all(id in ids)
            print(u)
            print("Exito en la actualizacion de etiquetas")
        except Exception as e: print(e)

        self.context['ids'] = ids
        all_posts = Evento.objects.all()
        self.context['posts'] = all_posts
        #return redirect("Eventos:listaEventos")
        return render(request, self.template, self.context)

