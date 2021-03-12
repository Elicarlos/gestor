from rest_framework import serializers
from core.models import Cursos


class CursosSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    descricao = serializers.CharField(required=False, max_length=100 )
    preco = serializers.DecimalField(required=False, max_digits=100, decimal_places=2)

    def create (self, validate_data):
        return Cursos.objects.create(**validate_data)


    def update(self, instance, validate_data):
        instance.decricao = validate_data.get('descricao', instance.descricao)
        instance.preco = validate_data.get('preco', instance.preco)
        instance.save()
        return instance