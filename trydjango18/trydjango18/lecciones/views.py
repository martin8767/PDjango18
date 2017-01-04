from django.shortcuts import render

# Create your views here.
def homel(request):
    return render(request, "lecciones.html", {})


def leccion1(request):
    return render(request, "lecciones/leccion1.html", {})
