from rest_framework import serializers
from .models import Cloud

class CloudSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('id', 'owner', 'name', 'description', 'updated_at', 'created_at')
    model = Cloud