from django.shortcuts import render

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
    imc = 1
    return render(request, "ejemplo/imc.html", {"imc": imc})