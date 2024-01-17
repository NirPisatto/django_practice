from typing import Any
from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')

# Create your models here.
class File(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    service_name = models.CharField(max_length=200)
    resource_type = models.CharField(max_length=200)
    uuid = models.CharField(max_length=200)
    guid = models.CharField(max_length=200)
    path = models.CharField(max_length=300)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
