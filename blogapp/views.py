from django.shortcuts import render


# Create your views here.
# CRIANDO METODOS

def index(request):
    return render(request, 'blog/index.html')
