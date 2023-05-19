from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    description = serializers.CharField()
    status = serializers.BooleanField()

    class Meta:
        fields = ['id', 'name', 'description', 'status']

class TaskSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    task_name = serializers.CharField()
    description = serializers.CharField()
    status = serializers.BooleanField()
    class Meta:
        fields = ['id', 'task_name', 'description', 'status']