from typing import Any
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect
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


class DetailView(generic.ListView):
    template_name = 'users/detail.html'
    context_object_name = 'rols_list'
    
    def get_queryset(self):
        ''' Returnthe all registered rols '''
        return Rol.objects.all()
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        # Call the base implementation first to get a context
        context = super(DetailView, self).get_context_data(**kwargs)
        # Get the user from id and add it to the context
        user_id = self.kwargs['pk']
        context['user'] = User.objects.get(pk=user_id)
        return context


def update(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    rol = get_list_or_404(Rol)
    try:
        selected_rol = Rol.objects.get(pk=request.POST['rol'])
    except (KeyError, Rol.DoesNotExist, User.DoesNotExist):
        context = {'user': user, 'rols_list': rol, 'error_message': 'No elegiste un rol. Intenta de nuevo.'}
        return render(request, 'users/detail.html', context)
    else:
        user.rol = selected_rol
        user.save()
        return HttpResponseRedirect(reverse('users:detail', args=(user.id,)))
    

class RegistrationView(generic.FormView):
    pass
