from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.views import LoginView
from django.views.generic.edit import  FormView
from django.shortcuts import render

class CusLoginView(LoginView):
    template_name='login.html'
    fields='__all__'
    redirect_authenticated_user= True

    def get_success_url(self):
        return reverse_lazy('intro')
    

class RegPage(FormView):
    form_class = UserCreationForm
    template_name = 'register.html'  # Your registration template
    success_url = reverse_lazy('intro')  # Redirect after successful registration

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # Automatically log in the user
        return super().form_valid(form)
   

# Create your views here.
class IntroView(LoginRequiredMixin, View):
    login_url = '/login/' 

    def get(self, request, *args, **kwargs):
        return render(request, 'intro.html')