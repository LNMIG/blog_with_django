from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'users'

urlpatterns = [
    path('userindex/', views.UserIndexView.as_view(), name='user_index'),
    path('rolindex/', views.RolIndexView.as_view(), name='rol_index'),
    path('detail/<int:pk>', views.DetailView.as_view(), name='detail'),
    path('registration/<int:pk>', views.RegistrationView.as_view(), name='registration'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)