from django.shortcuts import render
from .models import Song

# Create your views here.
def index(request):
    Songs = Song.objects.all().order_by('-uploaded_at')
    context = {'songs': Songs}
    return render(request, 'music/index.html', context)
