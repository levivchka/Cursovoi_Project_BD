from django.shortcuts import render 
from .models import Task
from .models import Shedule
# Create your views here.


def index(request):
    return render(request,'main/index.html')

def about(request):
    tasks = Task.objects.all()
    return render(request,'main/about.html', {'title': 'О сайте', 'tasks': tasks})  

def shedule(request):
    schedule_list = Shedule.objects.all()  # Здесь используется имя модели с заглавной буквы
    return render(request, 'main/shedule.html', {'schedule_list': schedule_list})
    