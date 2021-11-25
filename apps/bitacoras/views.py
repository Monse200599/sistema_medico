from django.shortcuts import render, redirect, get_object_or_404
from apps.bitacoras.forms import BitacoraForm
from apps.bitacoras.models import Bitacora


def listar_bitacoras(request):
    bitacoras = Bitacora.objects.all()
    data = {
        'bitacoras': bitacoras
    }
    return render(request, 'bitacoras/index.html', data)


def agregar_bitacora(request):
    data = {
        'form': BitacoraForm()
    }
    if request.method == "POST":
        formulario = BitacoraForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensajes"] = "Bitacora agregada correctamente"
            return redirect(to="listar_bitacoras")
        else:
            data["form"] = formulario
    return render(request, 'bitacoras/create.html', data)


def actualizar_bitacora(request, pk):
    bitacora = get_object_or_404(Bitacora, pk=pk)
    data = {
        'form': BitacoraForm(instance=bitacora)
    }
    if request.method == 'POST':
        formulario = BitacoraForm(data=request.POST, instance=bitacora)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_bitacoras")
        data["form"] = formulario
    return render(request, 'bitacoras/update.html', data)


def eliminar_bitacora(request, pk):
    bienes = get_object_or_404(Bitacora, pk=pk)
    bienes.delete()
    return redirect(to="listar_bitacoras")
