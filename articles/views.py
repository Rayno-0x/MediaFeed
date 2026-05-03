from django.shortcuts import render
from .models import Article

# Create your views here.

def index(request):
    Articles = Article.objects.all().order_by('-date_published')
    context = {'articles': Articles}
    return render(request, 'articles/index.html', context)
