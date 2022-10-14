from django.shortcuts import render
from ejemplo.models import Familiar

def index(request):
    return render(request, "ejemplo/saludar.html",
    {
    "nombre": "Ezequiel",
    "apellido": "Arias",
    })

def index_tres(request):
    return render(request, "ejemplo/saludar.html",
    {
    "notas": [1,2,3,4,5,6,7]}
    )

def imc(request, peso ,altura):
    altura_en_metros = altura / 100
    preso_en_kilos = peso / 100
    imc = preso_en_kilos / altura_en_metros * altura_en_metros
    
    return render(request, "ejemplo/imc.html", {"imc": imc})

def monstrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html", 
                {"lista_familiares": lista_familiares})