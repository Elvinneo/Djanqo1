from django.shortcuts import render,redirect,get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home__view(request):
    articles = Article.objects.all()
    return render(request,'index.html', {'articles': articles})

def dashboard__view(request):
    articles = Article.objects.filter(author=request.user)
    return render(request,'dashboard.html', {'articles': articles})



@login_required(login_url="account:login")
def articles__view(request):
    articles = Article.objects.all()
    return render(request,'articles.html', {'articles': articles})




@login_required(login_url="account:login")
def detail__view(request,id):
    # article = Article.objects.filter(id=id).first()

    article=get_object_or_404(Article,id=id)
    context={'article':article}
    return render(request,'detail.html',context)

@login_required(login_url="account:login")
def add__article__view(request):
    form=ArticleForm(request.POST or None,request.FILES or None)
    if form.is_valid():

        article=form.save(commit=False)
        article.author=request.user
        article.save()
        messages.success(request,"Məqaləniz qeyd edildi ")
        return redirect("dashboard")


    context={"form":form}
    return render(request,'addarticle.html',context)