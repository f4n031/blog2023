from django.contrib import admin
from django.urls import path
#CHAMA A PÁGINA
from blogapp.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index , name ='index'),
]
