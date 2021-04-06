from django.shortcuts import render, redirect
from .models import Category, Photo
# Create your views here.


def Home(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                name=data['category_new'])
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
                category=category,
                topic = data['category_new'],
                description=data['description'],
                image=image,
            )

        return redirect('allphotos')

    context = {'categories': categories}

    return render(request, 'multiple/home.html', context)


def allphotos(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'multiple/allphotos.html', context)
