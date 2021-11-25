from django.shortcuts import render, redirect, get_object_or_404
from apps.puestos.forms import PuestoForm
from apps.puestos.models import Puesto


def listar_puestos(request):
    puestos = Puesto.objects.all()
    data = {
        'puestos': puestos
    }
    return render(request, 'puestos/index.html', data)


def agregar_puesto(request):
    data = {
        'form': PuestoForm()
    }
    if request.method == "POST":
        formulario = PuestoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensajes"] = "Puesto agregada correctamente"
            return redirect(to="listar_puestos")
        else:
            data["form"] = formulario
    return render(request, 'puestos/create.html', data)


def actualizar_puesto(request, pk):
    puesto = get_object_or_404(Puesto, pk=pk)
    data = {
        'form': PuestoForm(instance=puesto)
    }
    if request.method == 'POST':
        formulario = PuestoForm(data=request.POST, instance=puesto)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_puestos")
        data["form"] = formulario
    return render(request, 'puestos/update.html', data)


def eliminar_puesto(request, pk):
    bienes = get_object_or_404(Puesto, pk=pk)
    bienes.delete()
    return redirect(to="listar_puestos")
