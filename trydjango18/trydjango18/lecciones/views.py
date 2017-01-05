from django.shortcuts import render

# Create your views here.
def homel(request):
    return render(request, "lecciones.html", {})


def leccion1vocabulario(request):
    tipo = {
        "gg" : "vocabulario",
    }
    return render(request, "lecciones/leccion1.html", tipo)

def leccion2vocabulario(request):
    tipo = {
        "gg" : "vocabulario",
    }
    return render(request, "lecciones/leccion2.html", tipo)

def leccion3vocabulario(request):
    tipo = {
        "gg" : "vocabulario",
    }
    return render(request, "lecciones/leccion3.html", tipo)

def leccion4vocabulario(request):
    tipo = {
        "gg" : "vocabulario",
    }
    return render(request, "lecciones/leccion4.html", tipo)

def leccion2(request):
    return render(request, "lecciones/leccion2.html", {})
