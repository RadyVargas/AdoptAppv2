from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.inicio, name='inicio'), 
    path('animales/', views.lista_animales, name='lista_animales'),
    path("contacto/", views.lista_contactos, name="lista_contactos"),
    path('adoptar/<int:animal_id>/', views.adoptar_animal, name='adoptar_animal'),
    # path('api-animales/', views.api_animales, name='api_animales'),  # <- puedes comentar o eliminar
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('registro/', views.registro, name='registro'),
]
