# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin
from apps.areas.models import Area

class AreasListado(ListView): 
    model = Area

class AreaDetalle(DetailView): 
    model = Area

class AreaCrear(SuccessMessageMixin, CreateView): 
    model = Area
    form = Area
    fields = ['nombre']
    success_message = 'Area crear correctamente!' # Mostramos este Mensaje luego de Crear un Area     

    # Redireccionamos a la página principal luego de crear un registro o Area
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer' 

class AreaActualizar(SuccessMessageMixin, UpdateView): 
    model = Area
    form = Area
    fields = ['nombre']
    success_message = 'Area actualizada Correctamente !' # Mostramos este Mensaje luego de Editar un Area 

    # Redireccionamos a la página principal luego de actualizar un registro o Area
    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer' 

class AreaEliminar(SuccessMessageMixin, DeleteView): 
    model = Area 
    form = Area
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o Area
    def get_success_url(self): 
        success_message = 'Area eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Area 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'     
