from django.shortcuts import render

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from user.forms import UserEditForm, UserRegisterForm
from user.models import Imagen
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.

def login_request(request):
    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                messages.success(request, f"¡Bienvenido, {usuario}!")
                
                return render(request, "AppEntrega3/mensaje.html", {"usuario": usuario})

        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})

def register(request):
    msg_register = ""
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
           
            form.save()
            return render(request,"AppEntrega3/index.html")
        else:
            msg_register = "Error en los datos ingresados"
            msg_register += f" | {form.errors}"

    form = UserRegisterForm()     
    return render(request,"users/registro.html" ,  {"form":form, "msg_register": msg_register})

@login_required 

def editarPerfil(request):
    usuario = request.user

    if request.method == 'POST': 

        miFormulario = UserEditForm(request.POST, request.FILES, instance=usuario)

        if miFormulario.is_valid():
            nueva_imagen = miFormulario.cleaned_data.get('imagen') 

            if nueva_imagen:
            
                if Imagen.objects.filter(user=usuario).exists():

                    avatar = Imagen.objects.get(user=usuario)
                    avatar.imagen = nueva_imagen
                    avatar.save()
                    messages.success(request, 'Registro exitoso. ¡Ahora puedes iniciar sesión!')


                else:
                    
                    avatar = Imagen(user=usuario, imagen=nueva_imagen)
                    avatar.save()
            miFormulario.save()

            return render(request, "AppEntrega3/index.html")

    else: 
        miFormulario = UserEditForm(instance=usuario)
    return render(request, "users/editarusuario.html", {"mi_form": miFormulario, "usuario": usuario})


class CambiarContrasenia(LoginRequiredMixin,SuccessMessageMixin, PasswordChangeView):
    template_name = "users/cambiarcontrasenia.html"
    success_url = reverse_lazy("inicio")
    success_message = "¡Tu contraseña ha sido cambiada con éxito!"

