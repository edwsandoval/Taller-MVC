from django.shortcuts import render,redirect

from .models import persona
from .models import ciudad
from .models import tipodocumento

def inicio(request):  
    personas = persona.objects.all() 
    ciudades = ciudad.objects.all()
    tipodocumentos = tipodocumento.objects.all()
    contexto ={'personas':personas,'ciudades':ciudades,'tipodocumentos':tipodocumentos}
    return render(request,'index.html',contexto)

    

def crearPersona(request):
    ciudades = ciudad.objects.all()
    tipodocumentos = tipodocumento.objects.all()
    contexto ={'ciudades':ciudades,'tipodocumentos':tipodocumentos}
    if request.method=='POST':
        p=persona()
        p.nombres=request.POST['nombres']
        p.apellidos=request.POST['apellidos']
        p.correo=request.POST['correo']
        p.telefono=request.POST['telefono']
        p.documento=request.POST['documento']
        p.usuario=request.POST['usuario']
        p.fechaNacimiento=request.POST['fechaNacimiento']
        p.contraseña=request.POST['contraseña']
        p.idTipoDocumento=tipodocumento.objects.get(pk=request.POST['tipoDocumento'])
        p.lugarResidencia=ciudad.objects.get(pk=request.POST['ciudad'])
        p.save()
        return redirect('index')
 
    return render(request,'crear_persona.html',contexto)

