from django.shortcuts import render, redirect
from .models import Animal 
from .models import Contacto
from django.shortcuts import get_object_or_404, redirect
import requests
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistroForm


def inicio(request):
    mensaje = "¡Bienvenido a AdoptApp! Encuentra a tu mejor amigo peludo."
    contexto = {"mensaje": mensaje}
    return render(request, 'index.html', contexto)


def lista_animales(request):
    animales = Animal.objects.all()

    tipo = request.GET.get("tipo")
    tamano = request.GET.get("tamano")
    edad = request.GET.get("edad")

    if tipo:
        animales = animales.filter(tipo__iexact=tipo)  # <-- iexact para mayúsc/minúsc

    if tamano:
        animales = animales.filter(tamano__iexact=tamano)  # <-- iexact también

    if edad:
        if edad == "joven":
            animales = animales.filter(edad__lt=2)
        elif edad == "adulto":
            animales = animales.filter(edad__gte=2, edad__lte=7)
        elif edad == "senior":
            animales = animales.filter(edad__gt=7)
    print("Filtros aplicados:", tipo, tamano, edad)
    print("QuerySet filtrado:", list(animales))

    return render(request, "animales.html", {
        "animales": animales,
        "request": request
    })


@login_required(login_url='login')
def lista_contactos(request):
    contactos = Contacto.objects.all().order_by("-fecha")
    return render(request, "contacto.html", {"contactos": contactos})

@login_required(login_url='login')
def adoptar_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)

    if request.method == "POST":
        nombre = request.POST.get("nombre")
        correo = request.POST.get("correo")
        mensaje = request.POST.get("mensaje")

        Contacto.objects.create(
            nombre=nombre,
            correo=correo,
            mensaje=mensaje,
            animal=animal
        )
        return redirect("lista_contactos")  

    return render(request, "form_adopcion.html", {"animal": animal})








def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cuenta creada correctamente. Ahora puedes iniciar sesión.')
            return redirect('login') 
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})