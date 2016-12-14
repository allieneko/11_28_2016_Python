from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
import random

def goldCounter(request, random, location):
    if not 'gold' in request.session:
        request.session['gold'] = 0
        request.session['history'] = []
    request.session['gold'] = request.session['gold'] + random
    request.session['result'] = random
    request.session['location'] = location
    request.session['datetime'] = str(datetime.now())
    dictionary = {
        'class': "green" if random >= 0 else "red",
        'activity': "You went to the {} and {} {} gold at {}. Now you have {} gold.".format(request.session['location'],('lost','gained')[random >= 0], abs(random), request.session['datetime'], request.session['gold'])
        }
    request.session['history'].append(dictionary)

def index(request):
    return render(request, 'ninjagold2/index.html')

def money(request):
    if request.POST['building'] == 'farm':
        farmGold = random.randrange(10,21)
        goldCounter(request, farmGold, 'farm')
    if request.POST['building'] == 'cave':
        caveGold = random.randrange(5,11)
        goldCounter(request, caveGold, 'cave')
    if request.POST['building'] == 'house':
        houseGold = random.randrange(2,6)
        goldCounter(request, houseGold, 'house')
    if request.POST['building'] == 'casino':
        casinoGold = random.randrange(-50,51)
        goldCounter(request, casinoGold, 'casino')
    return redirect('gold:index')

def refresh(request):
    request.session.flush()
    return redirect('gold:index')
