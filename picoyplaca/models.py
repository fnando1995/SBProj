from django.db import models
from django.urls import reverse

class Car(models.Model):
    """
    Model created to perform as a Car Object
    """
    placa = models.CharField(max_length=7)
    color = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)

    def __str__(self):
        return self.placa

    def get_absolute_url(self):
        return reverse('index')