from django.db import models


class MainModel(models.Model):
    created_at = models.DateTimeField("Data de criação", auto_now_add=True)
    updated_at = models.DateTimeField(
        "Data de atualização", auto_now=True)

    class Meta:
        abstract = True
