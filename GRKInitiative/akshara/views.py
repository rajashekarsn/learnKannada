from django.shortcuts import render
from .models import Letters
import random
# Create your views here.

def homepage(request):
    letters = Letters.objects.all()
    listval = [i.letter for i in Letters.objects.all()]
    random_choices = random.sample(listval, 3)
    random_choice = random.choice(listval)
    context = {
        'letters': letters,
        'random_choices': random_choices,
        'random_choice': random_choice,
    }
    return render(request, 'akshara/home.html', context)

#  from akshara.models import Letters
# >>> listval = [i.letter for i in Letters.objects.all()]
# >>> random_choices= random.sample(listval,3)
# >>> random_choices
# ['ಉ', 'ಈ', 'ಆ']
# >>> random_choice = random.choice(listval)
# >>> random_choice

