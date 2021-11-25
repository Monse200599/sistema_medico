from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from apps.recetas.models import Receta
from apps.api.recetas.serializers import RecetaSerializer


class RecetaViewSet(ViewSet):

    def list(self, request):
        serializer = RecetaSerializer(Receta.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve(self, request, pk: int):
        try:
            bien = RecetaSerializer(Receta.objects.get(pk=pk))
            return Response(status=status.HTTP_200_OK, data=bien.data)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"mensaje": "Elemento no encontrado"})

    def create(self, request):
        serializer = RecetaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def update(self, request, pk: int):
        try:
            serializer = RecetaSerializer(Receta.objects.get(pk=pk), data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"mensaje": "Elemento no encontrado"})

    def destroy(self, request, pk: int):
        try:
            bien = Receta.objects.get(pk=pk)
            bien.delete()
            return Response(status=status.HTTP_202_ACCEPTED, data={"mensaje": "Eliminado correctamente"})
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"mensaje": "Elemento no encontrado"})
