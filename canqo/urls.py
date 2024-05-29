from django.contrib import admin
from django.urls import path
from article.views import home__view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home__view),
    path('admin/', admin.site.urls),
]


urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)