from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from .models import Article,Comment
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
    keyword= request.GET.get('keyword')
    if keyword:
        articles = Article.objects.filter( title__contains=keyword)
        return render(request,'articles.html', {'articles': articles})
    articles = Article.objects.all()
    return render(request,'articles.html', {'articles': articles})




@login_required(login_url="account:login")
def detail__view(request,id):
    # article = Article.objects.filter(id=id).first()
    comments=Comment.objects.all()
    article=get_object_or_404(Article,id=id)
    context={'article':article,
             'comments':comments}
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




@login_required(login_url="account:login")
def article__update__view(request,id):
    article=get_object_or_404(Article,id=id)
    form=ArticleForm(request.POST or None,request.FILES or None ,instance=article)
    if form.is_valid():
        # article=form.save(commit=False)
        # article.author=request.user
        article.save()
        messages.success(request,"Məqaləniz redaktə edildi ")
        return redirect("dashboard")
    context={"form":form}
    return render(request,'update.html',context)


@login_required(login_url="account:login")
def article__delete__view(request,id):
    article=get_object_or_404(Article,id=id)
    form=ArticleForm(request.POST or None,request.FILES or None, instance=article)
    article.delete()
    messages.success(request,"Məqaləniz silindi ")
    return redirect("dashboard")


    context={"form":form}
    return render(request,'delete.html',context)


@login_required(login_url="account:login")

def addcomment__view(request,id):
    article=get_object_or_404(Article,id=id)


    if request.method == "POST":
        comment_author=request.POST.get('comment_author')
        comment_content=request.POST.get('comment_content')

        newComment=Comment(comment_author=comment_author,comment_content=comment_content)
        newComment.article=article
        newComment.save()
        messages.success(request,"Şərhiniz əlavə olundu")
    return redirect(reverse('detail',kwargs={"id":id}))

