from django.shortcuts import render, redirect
from app.models import Socio
from app.forms import FormProyecto
# Create your views here.
def index(request):
    return render(request, 'index.html')

def listadoSocios(request):
    socios = Socio.objects.all()
    data = {'socios': socios}
    return render(request,'listadoSocios.html', data)

def agregarSocio(request):
    form = FormProyecto()
    if request.method == 'POST':
        form = FormProyecto(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request,'agregarSocio.html', data)

def eliminarsocio(request, id):
    socios = Socio.objects.get(id=id)
    socios.delete()
    return redirect('/socios')

def actualizarsocio(request, id):
    socios = Socio.objects.get(id = id)
    form = FormProyecto(instance = socios)
    if request.method == 'POST':
        form = FormProyecto(request.POST, instance=socios)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form':form}
    return render(request, 'agregarSocio.html', data)