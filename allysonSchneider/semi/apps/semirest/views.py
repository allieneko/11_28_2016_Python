from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from .models import Item

# Create your views here.
def index(request):
    context = {
        "items" : Item.objects.all(),
    }
    return render(request, "semirest/index.html", context)

def show(request, id):
    context = {
        "items" : Item.objects.filter(id=id),
        "id" : id,
    }
    return render(request, "semirest/show.html", context, id)

def new(request):
    return render(request, "semirest/new.html")

def edit(request, id):
    context = {
        "items" : Item.objects.filter(id=id),
        "id" : id,
    }
    return render(request, "semirest/edit.html", context, id)

def create(request):
    try:
        Item.objects.create(name=request.POST['name'], description=request.POST['description'], price=request.POST['price'])
    except (ValidationError):
        context = {
            "errors" : "Please enter a numerical value!",
        }
        return render(request, "semirest/new.html", context)
    return redirect('/products')

def update(request, id):
    try:
        Item.objects.filter(id=id).update(name=request.POST['name'], description=request.POST['description'], price=request.POST['price'])
    except (ValidationError):
        context = {
            "items" : Item.objects.filter(id=id),
            "errors" : "Please enter a numerical value!",
        }

        return render(request, "semirest/edit.html", context)
    return redirect('/products')

def destroy(request, id):
    Item.objects.get(id=id).delete()
    return redirect('/products')
