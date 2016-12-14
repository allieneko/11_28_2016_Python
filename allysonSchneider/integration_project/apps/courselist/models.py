from django.db import models
from ..loginreg.models import User
# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=1000)
    students = models.ManyToManyField(User, related_name = 'registered_students')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
