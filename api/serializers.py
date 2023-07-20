from rest_framework import serializers
from .models import ApiTable

class ApiTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiTable
        fields = '__all__'
