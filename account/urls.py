from django.urls import path
from .views import *

app_name='account'

urlpatterns = [

    path('registe', registe__view,name="registe"),
    path('login', login__view,name="login"),
    path('logout', logout__view,name="logout"),

]
