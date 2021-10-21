from django.shortcuts import render

# Create your views here.
# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.puestos.models import Puesto


@login_required(login_url="/login/")
def index(request):
    puestos = Puesto.objects.all()
    return render(request, 'puestos/index.html', {'puestos': puestos})
