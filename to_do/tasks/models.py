from django.db import models
from django.forms import ModelForm
# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title