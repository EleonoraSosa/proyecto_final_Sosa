from django.shortcuts import render,  get_object_or_404
from AppEntrega3.models import Registro, Ubicacion, Musica
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(req):
    return render(req, 'appentrega3/padre.html')

@login_required
def registro(req):
     return render(req, 'appentrega3/registro.html')


@login_required
def ubicacion(req):
     return render(req, 'appentrega3/ubicacion.html')


@login_required
def musica(req):
   return render(req, 'appentrega3/musica.html')

def acerca_de_mi(req):
    return render(req, 'appentrega3/acercademi.html')

def registro_Formulario(req):

    if req.method == 'POST':
        registro = Registro(nombre=req.POST['nombre'], apellido=req.POST['apellido'], email=req.POST['email'], edad=req.POST['edad'])
        registro.save()


        return render(req, 'AppEntrega3/registro.html')
    
def ubicacion_Formulario(req):

    if req.method == 'POST':
        ubicacion = Ubicacion(ciudad=req.POST['ciudad'], capital=req.POST['capital'], codigo_postal=req.POST["codigo_posta"])
        ubicacion.save()


        return render(req, 'AppEntrega3/ubicacion.html')
    
def musica_Formulario(req):
    if req.method == 'POST':
        pelicula = Musica(nombre=req.POST['nombre'], genero=req.POST['genero'], año=req.POST['año'])
        pelicula.save()

        return render(req, 'AppEntrega3/musica.html')
    
    
def busca_Informacion(req):
    return render  (req, "AppEntrega3/buscar_informacion.html")
    
def buscar(req):
    if req.GET.get("nombre"):  
        nombre = req.GET["nombre"]
        musicas = Musica.objects.filter(nombre__icontains=nombre)  

        return render(req, "AppEntrega3/musica.html", {
            "musicas": musicas,
            "nombre": nombre
        })
    else:
        return render(req, "AppEntrega3/musica.html")
    
@login_required
def leerMusica(req):

    musicas = Musica.objects.all() #trae todos las canciones

    contexto= {"musicas": musicas} 

    return render(req, "AppEntrega3/leerMusica.html",contexto)  
    
def FormularioMusica(req):
    if req.method == 'POST':
        nombre = req.POST.get('nombre')
        genero = req.POST.get('genero')
        año = req.POST.get('año')

        if nombre and genero and año:
            musica = Musica(nombre=nombre, genero=genero, año=año)
            musica.save()
            return render( req, "AppEntrega3/musica.html")  
    else:
        return render(req, 'AppEntrega3/musica.html')

def eliminarMusica(req, musica_nombre):
    musica = Musica.objects.filter(nombre=musica_nombre)
    musica.delete()

    # vuelvo al menú
    musicas = Musica.objects.all()  # trae todas las canciones

    contexto = {"musicas": musicas}

    return render(req, "AppEntrega3/leerMusica.html", contexto)

def editarMusica(req, musica_nombre):
    musica = get_object_or_404(Musica, nombre=musica_nombre)

    if req.method == 'POST':

        nombre = req.POST.get('nombre')
        genero = req.POST.get('genero')
        año = req.POST.get('año')

        if nombre and genero and año:
            musica.nombre = nombre
            musica.genero = genero
            musica.año = año

            musica.save()  
            return render(req, "AppEntrega3/musica.html")  

    return render(req, "AppEntrega3/editarMusica.html", {"musica": musica})




