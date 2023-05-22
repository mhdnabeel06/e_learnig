
# from app.models import Course
from django.shortcuts import render, redirect,get_object_or_404
from .models import Topic,Course
from .forms import CourseForm
from . import forms
from . forms import TopicForm 



# Create your views here.

def home(request):
    courses =Course.objects.all()
    context ={
        'courses':courses,
    }
    return render(request,'home.html',context)





def create(request):
    if request.method =='POST':
        form = CourseForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
            
    return render(request, 'create.html', {'form': forms})

def topics_list(request,pk):
    
    cource = get_object_or_404(Course,pk=pk)
    topics = cource.topics.all()
    context = {
        'topics':topics,
        'course':cource
    }
    
    return render(request,'class.html',context)

def topic_create(requset):
    if requset.method == 'POST':
        form = TopicForm(requset.POST,requset.FILES)
        if form.is_valid():
           form.save()
           return redirect('home')
        else:
             print(form.errors)
    else:
        form = TopicForm()
    return render(requset,'topic_create.html',{'form':form})
    
    
    
