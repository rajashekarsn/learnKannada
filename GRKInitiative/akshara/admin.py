from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models

from .models import Letters, Words4Letter, TextBox


class ChoiceInline(admin.StackedInline):
    model = Words4Letter
    extra = 3


# Register your models here.
class LettersAdmin(admin.ModelAdmin):
    list_display = ('letter',)
    inlines = [ChoiceInline]


class TextboxAdmin(admin.ModelAdmin):
    list_display = ('blog',)

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }


admin.site.register(Letters, LettersAdmin)
admin.site.register(TextBox, TextboxAdmin)
