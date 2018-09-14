from rest_framework import serializers

class MeuObjetoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nome = serializers.CharField(max_length=50)
    sobrenome = serializers.CharField(max_length=50) 