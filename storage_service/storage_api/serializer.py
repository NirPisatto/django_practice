from rest_framework import serializers
from storage_api.models import File
from .models import UploadedFile

class FileSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=200, allow_blank=True, required=False)
    service_name = serializers.CharField(max_length=200, allow_blank=True, required=False)
    resource_type = serializers.CharField(max_length=200, allow_blank=True, required=False)
    uuid = serializers.CharField(max_length=200, allow_blank=True, required=False)
    guid = serializers.CharField(max_length=200, allow_blank=True, required=False)
    path = serializers.CharField(max_length=300, allow_blank=True, required=False)

    def create(self, validated_data):
        return File.objects.create(**validated_data)
    
class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ('file',)