from django.shortcuts import render
from .models import Letters, TextBox, Words4Letter
import random
# Create your views here.


def homepage(request):
    # letters = Letters.objects.all()
    textbox = TextBox.objects.all()
    context = {
        # 'letters': letters,
        'textbox': textbox,
    }
    return render(request, 'akshara/home.html', context)


def words4letterpage(request):
    alphabet = Letters.objects.all()
    words_for_a_letter = Words4Letter.objects.all()
    context = {
        'words_for_a_letter': words_for_a_letter,
        'alphabet': alphabet,
    }
    return render(request, 'akshara/wordsforletter.html', context)


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


def random_eng_word(request):
    word = [i.english_word for i in Words4Letter.objects.all()]
    random_choice = random.choice(word)
    context = {
        'random_choice': random_choice,
    }
    return render(request, 'akshara/randomengword.html', context)


def random_kan_word(request):
    word = [i.word for i in Words4Letter.objects.all()]
    random_choice = random.choice(word)
    context = {
        'random_choice': random_choice,
    }
    return render(request, 'akshara/randomkanword.html', context)


def random_image(request):
    img = [i.word_image for i in Words4Letter.objects.all()]
    random_choice = random.choice(img)

    context = {
        'random_choice': random_choice,
    }
    return render(request, 'akshara/randomimage.html', context)
