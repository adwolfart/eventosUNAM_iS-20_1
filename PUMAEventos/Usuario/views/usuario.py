from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        return redirect('players:event_list')
        #if request.user.is_teacher:
         #   return redirect('teachers:quiz_change_list')
        #else:
         #   return redirect('students:quiz_list')
    return render(request, 'usuario/home.html')
