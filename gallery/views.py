from django.shortcuts import render, get_object_or_404
from .models import Photo

# Create your views here.
def index(request):
    Photos = Photo.objects.all().order_by('-created_at')
    context = {'photos': Photos}
    return render(request, 'gallery/index.html', context)
