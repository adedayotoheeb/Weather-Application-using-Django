from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=35, unique=True)

    def __str__(self):
        return str(self.name)
