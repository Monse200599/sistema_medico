from django.shortcuts import render, redirect, get_object_or_404
from apps.recetas.forms import RecetaForm
from apps.recetas.models import Receta


def listar_recetas(request):
    recetas = Receta.objects.all()
    data = {
        'recetas': recetas
    }
    return render(request, 'recetas/index.html', data)


def agregar_receta(request):
    data = {
        'form': RecetaForm()
    }
    if request.method == "POST":
        formulario = RecetaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensajes"] = "Receta agregada correctamente"
            return redirect(to="listar_recetas")
        else:
            data["form"] = formulario
    return render(request, 'recetas/create.html', data)


def actualizar_receta(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    data = {
        'form': RecetaForm(instance=receta)
    }
    if request.method == 'POST':
        formulario = RecetaForm(data=request.POST, instance=receta)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_recetas")
        data["form"] = formulario
    return render(request, 'recetas/update.html', data)


def eliminar_receta(request, pk):
    bienes = get_object_or_404(Receta, pk=pk)
    bienes.delete()
    return redirect(to="listar_recetas")
