from django.urls import path
from AppEntrega3 import views



urlpatterns = [
    path('', views.inicio, name='inicio' ),
    path('registro/', views.registro, name='registro' ),
    path('ubicacion/', views.ubicacion, name='ubicacion' ),
    path('musica/', views.musica, name='musica' ),
    path('registroFormulario/', views.registro_Formulario, name='registroForm' ),
    path('ubicacionFormulario/', views.ubicacion_Formulario, name='ubicacionForm' ),
    path('musicaFormulario/', views.musica_Formulario, name='musicaForm' ),
    path('buscarInformacion/', views.busca_Informacion, name='buscarForm' ),
    path('buscar/', views.buscar, name='buscar'),
    path('leerMusica/', views.leerMusica, name='leerMusica'),
    path('FormularioMusica/',views.FormularioMusica , name='FormMusica'),
    path('eliminarMusica/<musica_nombre>/',views.eliminarMusica, name='EliminarMusica'),
    path('editarMusica/<musica_nombre>/',views.editarMusica, name='editarMusica'),
    path('acercademi/', views.acerca_de_mi, name='acercademi' ),
    ]




