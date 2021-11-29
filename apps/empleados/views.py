from django.shortcuts import render, redirect, get_object_or_404
from apps.empleados.forms import EmpleadoForm
from apps.empleados.models import Empleado


def listar_empleados(request):
    empleados = Empleado.objects.all()
    data = {
        'empleados': empleados
    }
    return render(request, 'empleados/index.html', data)


def agregar_empleado(request):
    data = {
        'form': EmpleadoForm()
    }
    if request.method == "POST":
        formulario = EmpleadoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensajes"] = "Empleado agregado correctamente"
            return redirect(to="listar_empleados")
        else:
            data["form"] = formulario
    return render(request, 'empleados/create.html', data)


def actualizar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    data = {
        'form': EmpleadoForm(instance=empleado)
    }
    if request.method == 'POST':
        formulario = EmpleadoForm(data=request.POST, instance=empleado)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_empleados")
        data["form"] = formulario
    return render(request, 'empleados/update.html', data)


def eliminar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    empleado.delete()
    return redirect(to="listar_empleados")
