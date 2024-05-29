from django.shortcuts import render
from .models import Article


def home__view(request):
    articles = Article.objects.all()
    return render(request,'index.html', {'articles': articles})