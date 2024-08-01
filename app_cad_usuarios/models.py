from django.db import models

class Usuario(models.Model):
    id_usuario = models.BigAutoField(primary_key=True)
    name_usuario = models.TextField(max_length=255)
    age_usuario = models.IntegerField()