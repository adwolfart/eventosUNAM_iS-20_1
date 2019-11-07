from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from .utils import IsNotAuthenticatedMixin
#from Post.models import Post
from .forms import LoginForm, OrgForm, DelForm, UserProfileForm


from django.contrib.auth.models import User
from django.core.mail import send_mail
from Home.models import UserProfile


from django.contrib.auth.forms import PasswordResetForm


# Function Views
def index(request):
    """
        Index in my Web Page.
    """
    print(request.method)
    template = 'Home/index.html'
    context = {}
    return render(request, template, context)



# Class-based Views
class Index(View):
    """
        Index in my Web Page but with Clased based views.
    """
    template = 'Home/index.html'
    context = {'title': 'Index'}

    def get(self, request):
        """
            Get in my Index.
        """
        #all_posts = Post.objects.all()
        #self.context['posts'] = all_posts
        return render(request, self.template, self.context)
        

class RegistrarU(View):
    """
        Index in my Web Page but with Clased based views.
    """
    template = 'Home/registrarU.html'
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
        form = UserProfileForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            avatar = request.POST.get('avatar', '')
            print(avatar)
            try:

                nombre = request.POST.get('nombre', '')
                correo = request.POST.get('correo', '')
                password = request.POST.get('password', '')
                entidad = request.POST.get('entidad', '')
                avatar = request.FILES.get('avatar', '')
                print(avatar)

                user = User.objects.create_user(username = correo, password = password, email = correo, first_name = 'Estudiante', last_name = nombre)
                userprofile = UserProfile.objects.create( user = user, nombre = nombre,  entidad = entidad)  
                try:
                    userprofile.avatar = avatar
                    userprofile.save()
                except: 
                    print("Error al upload")
                send_mail(
                'Confirmacion de cuenta',
                'Da click para confirmar tu registro',
                'pumaeventosunam@gmail.com',
                [correo],
                fail_silently=False,
                )            
            except Exception as e: print(e)  
            print("exito en el registro") 
        else:
            print("registro invalido")    


        self.context['form'] = form

        return redirect("Home:login")
        #return render(request, self.template, self.context)


class Home(View):
    """
        Index in my Web Page but with Clased based views.
    """
    template = 'Home/home.html'
    context = {'title': 'Index'}

    def get(self, request):
        """
            Get in my Index.
        """
        #all_posts = Post.objects.all()
        #self.context['posts'] = all_posts
        return render(request, self.template, self.context)




class RegistrarO(View):
    """
        Index in my Web Page but with Clased based views.
    """
    template = 'Home/registrarO.html'
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
        form = OrgForm(request.POST)
        if form.is_valid():

            try:

                user = User.objects.create_user(username=form.cleaned_data['correo'],email=form.cleaned_data['correo'],password='default', last_name = form.cleaned_data['nombre'], first_name = 'Organizador')            
                send_mail(
                'Crea contraseña',
                'Da click para establecer tu contraseña',
                'pumaeventosunam@gmail.com',
                [user.email],
                fail_silently=False,
                )
            except Exception as e: print(e)


        self.context['form'] = form

        return redirect("Home:home")
        #return render(request, self.template, self.context)

def del_user(request, username):    
    try:
        u = User.objects.get(username = username)
        u.delete()
        print( "The user is deleted")
    except:
        print(request, "The user not found")    
    return redirect("Home:home")

class EliminarO(View):
    """
        Index in my Web Page but with Clased based views.
    """
    template = 'Home/eliminarO.html'
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
        form = DelForm(request.POST)
        if form.is_valid():
                del_user(request, username=form.cleaned_data['correo'])

        self.context['form'] = form
        send_mail(
        'Subject here',
        'Here is the message.',
        'pumaeventosunam@gmail.com',
        ['ori@ciencias.unam.mx'],
        fail_silently=False,
        )
        return redirect("Home:home")
        #return render(request, self.template, self.context)


class About(View):
    """
        About me page.
    """
    template = 'Home/about.html'
    context = {'title': 'About me'}

    def get(self, request):
        """
            Get in About me.
        """
        return render(request, self.template, self.context)


class Login(IsNotAuthenticatedMixin, View):
    """
        Admin login
    """
    template = 'Home/login.html'
    context = {'title': 'Admin Login'}

    def get(self, request):
        """
            Shows the form to login
        """
        form = LoginForm()
        self.context['form'] = form

        return render(request, self.template, self.context)

    def post(self, request):
        """
            Validates and do the login
        """
        form = LoginForm(request.POST)
        print(form)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            print(user)
            if user is not None:
                print(user)
                login(request, user)
                if request.GET.get("next", None) is not None:
                    return redirect(request.GET.get("next"))
                
                return redirect("Home:home")

        self.context['form'] = form
        return render(request, self.template, self.context)


class Logout(LoginRequiredMixin, View):
    """
        Does the logout
    """
    def get(self, request):
        logout(request)
        return redirect("Home:index")
