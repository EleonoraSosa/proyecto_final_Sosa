from django.urls import path
from  user import views
from django.contrib.auth.views import LogoutView




urlpatterns = [
    path('login/', views.login_request, name='login' ),
    path('register/', views.register, name='register' ),
    path('logout/', LogoutView.as_view(template_name='AppEntrega3/index.html'), name="logout"),
    path('editarPerfil/', views.editarPerfil, name='editarperfil' ),
    path('cambiarContrasenia/', views.CambiarContrasenia.as_view(), name='cambiarcontrasenia' ),

    ]

