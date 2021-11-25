from django.shortcuts import render, redirect, get_object_or_404
from apps.areas.forms import AreasForm
from apps.areas.models import Area

def listar_areas(request):
    areas = Area.objects.all()
    data = {
        'areas': areas
    }
    return render(request, 'areas/index.html', data)

def agregar_area(request):
    data = {
        'form': AreasForm()
    }
    if request.method == "POST":
        formulario = AreasForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensajes"] = "Area agregada correctamente"
            return redirect(to="listar_areas")
        else:
            data["form"] = formulario
    return render(request, 'areas/create.html', data)

def actualizar_area(request, pk):
    area = get_object_or_404(Area, pk=pk)
    data = {
        'form': AreasForm(instance=area)
    }
    if request.method == 'POST':
        formulario = AreasForm(data=request.POST, instance=area)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_areas")
        data["form"] = formulario
    return render(request, 'areas/update.html', data)

def eliminar_area(request, pk):
    area = get_object_or_404(Area, pk=pk)
    area.delete()
    return redirect(to="listar_areas")
