from django.shortcuts import render



def gallery(request):
    return render(request, 'photos/gallery.html')

def viewPhoto(request):
    return render(request, 'photos/add.html')

def addPhoto(request, pk):
    return render(request, 'photos/photo.html')
