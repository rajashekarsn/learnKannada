import os

from django.core.files.storage import FileSystemStorage
from django.db import models


# Create your models here.
class Letters(models.Model):
    letter = models.CharField(max_length=30)

    def __str__(self):
        return self.letter


class OverwriteStorage(FileSystemStorage):

    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join('', name))
        return name


fs = OverwriteStorage(location='')


class Words4Letter(models.Model):
    word = models.CharField(max_length=30)
    english_word = models.CharField(max_length=30)
    letter = models.ForeignKey(Letters, on_delete=models.CASCADE)
    word_image = models.ImageField(upload_to='media/img', blank=True, storage=fs)

    def __str__(self):
        return self.word


class TextBox(models.Model):
    blog = models.CharField(max_length=30)
    textbox = models.TextField(max_length=5000)

    def __str__(self):
        return self.textbox
