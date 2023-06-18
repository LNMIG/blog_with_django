from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import User, Rol

# Create your views here.

class UserIndexView(generic.ListView):
    template_name = 'users/user_index.html'
    context_object_name = 'users_list'

    def get_queryset(self):
        ''' Returnthe all registered users '''
        return User.objects.all()

class RolIndexView(generic.ListView):
    template_name = 'users/rol_index.html'
    context_object_name = 'rols_list'

    def get_queryset(self):
        ''' Returnthe all registered rols '''
        return Rol.objects.all()


class DetailView(generic.DetailView):
    pass

class RegistrationView(generic.FormView):
    pass
