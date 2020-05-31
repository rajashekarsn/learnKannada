from django.contrib import admin
from .models import Letters, TextBox

# Register your models here.
class LettersAdmin(admin.ModelAdmin):
    list_display = ('letter',)



admin.site.register(Letters, LettersAdmin)