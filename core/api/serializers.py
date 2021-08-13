from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from rest_framework import serializers

class PontoTuristicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = ("id", "nome", "descricao")