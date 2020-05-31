from django.shortcuts import render
from .models import Letters
import random
# Create your views here.

def homepage(request):
    letters = Letters.objects.all()
    context = {
        'letters': letters,
    }
    return render(request, 'akshara/home.html', context)


def viewletters(request):
    atoaha = Letters.objects.filter(id__lt=16)
    kaline = Letters.objects.filter(id__range=(16, 20))
    chaline = Letters.objects.filter(id__range=(21, 25))
    taline = Letters.objects.filter(id__range=(26, 30))
    thaline = Letters.objects.filter(id__range=(31, 35))
    paline = Letters.objects.filter(id__range=(36, 40))
    yaline = Letters.objects.filter(id__range=(41, 49))
    context = {
        'atoaha': atoaha,
        'kaline': kaline,
        'chaline': chaline,
        'taline': taline,
        'thaline': thaline,
        'paline': paline,
        'yaline': yaline,
    }
    return render(request, 'akshara/letters.html', context)


def randomletter(request):
    listval = [i.letter for i in Letters.objects.all()]
    random_choice = random.choice(listval)
    context = {
        'random_choice': random_choice,
    }
    return render(request, 'akshara/randomletter.html', context)


def randomletters(request):
    listval = [i.letter for i in Letters.objects.all()]
    random_choices = random.sample(listval, 5)
    context = {
        'random_choices': random_choices,
    }
    return render(request, 'akshara/randomletters.html', context)


