from django.shortcuts import render, redirect, get_object_or_404
from apps.bienes.forms import BienesForm
from apps.bienes.models import Bienes


def listar_bienes(request):
    bienes = Bienes.objects.all()
    data = {
        'bienes': bienes
    }
    return render(request, 'bienes/index.html', data)


def agregar_bienes(request):
    data = {
        'form': BienesForm()
    }
    if request.method == "POST":
        formulario = BienesForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensajes"] = "Bien agregado correctamente"
            return redirect(to="listar_bienes")
        else:
            data["form"] = formulario
    return render(request, 'bienes/create.html', data)


def actualizar_bienes(request, pk):
    bienes = get_object_or_404(Bienes, pk=pk)
    data = {
        'form': BienesForm(instance=bienes)
    }
    if request.method == 'POST':
        formulario = BienesForm(data=request.POST, instance=bienes)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_bienes")
        data["form"] = formulario
    return render(request, 'bienes/update.html', data)


def eliminar_bienes(request, pk):
    bienes = get_object_or_404(Bienes, pk=pk)
    bienes.delete()
    return redirect(to="listar_bienes")
