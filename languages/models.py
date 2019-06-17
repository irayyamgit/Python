from django.db import models


# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=250)
    paradigm = models.CharField(max_length=250)

    def __str__(self):
        return self.name
