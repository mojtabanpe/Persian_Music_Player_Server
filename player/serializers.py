from rest_framework import serializers
from .models import Music

class MusicSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    source = serializers.CharField()

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.source = validated_data.get('source', instance.source)
        instance.save()
        return instance

    def create(self, validated_data):
        return Music.objects.create(**validated_data)