from typing import Any
from django.db import models

# Create your models here.
class File(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=False)
    service_name = models.CharField(max_length=200, null=False)
    resource_type = models.CharField(max_length=200, null=False)
    uuid = models.CharField(max_length=200, null=False)
    guid = models.CharField(max_length=200, null=False)
    file = models.FileField(upload_to='uploads/')
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
