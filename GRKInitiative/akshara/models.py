from django.db import models


# Create your models here.
class Letters(models.Model):
    letter = models.CharField(max_length=30)

    def __str__(self):
        return self.letter


class TextBox(models.Model):
    textbox = models.TextField(max_length=300)

    def __str__(self):
        return self.textbox
