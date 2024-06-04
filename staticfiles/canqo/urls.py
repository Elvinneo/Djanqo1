from django.contrib import admin
from django.urls import path,include
from article.views import *
from account.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home__view,name="home"),
    path('account/',include('account.urls'),name="account"),
    path('admin/', admin.site.urls,name='admin'),
    path('contact/', contact__view,name='contact'),
    path('articles',articles__view,name='articles'),
    path('addarticle',add__article__view,name='addarticle'),
    path('detail/<int:id>',detail__view,name='detail'),
    path('dashboard',dashboard__view,name='dashboard'),
    path('about/', About__view,name='about'),
   
]


urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)