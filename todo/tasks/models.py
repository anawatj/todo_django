from uuid import uuid4
from django.db import models

class Task(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    name = models.CharField(max_length=100,null=True,blank=True)
    subject = models.CharField(max_length=100,null=True,blank=True)
    detail = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name
