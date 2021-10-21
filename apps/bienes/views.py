# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from apps.bienes.models import Bienes


class BienesListado(ListView):
    model = Bienes


class BienesDetalle(DetailView):
    model = Bienes


class BienesCrear(SuccessMessageMixin, CreateView):
    model = Bienes
    form = Bienes
    fields = ['tipo', 'num_unidades', 'num_cajas', 'lote',
              'caducidad', 'tipo_bienes', 'codigo_barras']
    # Mostramos este Mensaje luego de Crear un Bienes
    success_message = 'Bienes crear correctamente!'

    # Redireccionamos a la página principal luego de crear un registro o Bienes
    def get_success_url(self):
        return reverse('leer')  # Redireccionamos a la vista principal 'leer'


class BienesActualizar(SuccessMessageMixin, UpdateView):
    model = Bienes
    form = Bienes
    fields = ['tipo', 'num_unidades', 'num_cajas', 'lote',
              'caducidad', 'tipo_bienes', 'codigo_barras']

    # Mostramos este Mensaje luego de Editar un Bienes
    success_message = 'Bienes actualizada Correctamente !'

    # Redireccionamos a la página principal luego de actualizar un registro o Bienes
    def get_success_url(self):
        return reverse('leer')  # Redireccionamos a la vista principal 'leer'


class BienesEliminar(SuccessMessageMixin, DeleteView):
    model = Bienes
    form = Bienes
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o Bienes
    def get_success_url(self):
        # Mostramos este Mensaje luego de Editar un Bienes
        success_message = 'Bienes eliminado Correctamente !'
        messages.success(self.request, (success_message))
        return reverse('leer')  # Redireccionamos a la vista principal 'leer'
