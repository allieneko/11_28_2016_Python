from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    context = {

    }
    return render(request, 'disappearingninja/index.html', context)

def ninja(request, color):
    context = {
        'color': color,
    }
    return render(request, 'disappearingninja/ninja.html', context)


def ninjas(request):

    context = {
        'ninjas': 'cow',
    }
    print context
    return render(request, 'disappearingninja/ninja.html', context)
