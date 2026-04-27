from django.shortcuts import render


# Create your views here.
def principal(request):
    alumnos = Alumnos.objects.all()
    return render(request,"inicio/principal.html", {"alumnos": alumnos})


def contacto(request):
    return render(request,"inicio/contacto.html")


from registros.models import Alumnos

def formulario(request):
    if request.method == 'POST':
        matricula = request.POST.get('matricula')
        nombre = request.POST.get('nombre')
        carrera = request.POST.get('carrera')
        turno = request.POST.get('turno')
        imagen = request.FILES.get('imagen')
        
        alumno = Alumnos(
            matricula=matricula,
            nombre=nombre,
            carrera=carrera,
            turno=turno,
            imagen=imagen
        )
        alumno.save()
        return render(request, "inicio/formulario.html", {'mensaje': '¡Alumno registrado exitosamente!'})
        
    return render(request,"inicio/formulario.html")

def ejemplo(request):
    return render(request,"inicio/ejemplo.html")

def seguridad(request):
    return render(request,"inicio/seguridad.html")