from django.db import models


# Create your models here.
class Letters(models.Model):
    letter = models.CharField(max_length=30)

    def __str__(self):
        return self.letter


class a(models.Model):
    letter = models.CharField(max_length=30)

    def __str__(self):
        return self.letter