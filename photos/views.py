from django.shortcuts import render
from .models import Category, Photo


def gallery(request):
    photos = Photo.objects.all()
    categories = Category.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'photos/gallery.html', context)

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photo': photo})

def addPhoto(request):
    return render(request, 'photos/add.html')

