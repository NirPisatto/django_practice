from rest_framework import serializers
from storage_api.models import File

class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('file', 'name', 'description', 'service_name', 'resource_type', 'uuid', 'guid', 'file')
        extra_kwargs = {
            'name': {'required': False},
            'description': {'required': False},
            'service_name': {'required': False},
            'resource_type': {'required': False},
            'uuid': {'required': False},
            'guid': {'required': False},
            'file': {'required': False},
        }


# class FileSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=100)
#     description = serializers.CharField(max_length=200, allow_blank=True, required=False)
#     service_name = serializers.CharField(max_length=200, allow_blank=True, required=False)
#     resource_type = serializers.CharField(max_length=200, allow_blank=True, required=False)
#     uuid = serializers.CharField(max_length=200, allow_blank=True, required=False)
#     guid = serializers.CharField(max_length=200, allow_blank=True, required=False)
#     file = serializers.CharField(max_length=300, allow_blank=True, required=False)

    def create(self, validated_data):
        return File.objects.create(**validated_data)