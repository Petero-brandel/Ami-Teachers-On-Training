from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomSignupForm, LessonForm, ModuleForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Module, Lesson


def sign_up(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('login') 
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
       
        form = CustomSignupForm()

    return render(request, 'registration/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('course-page')  
        else:
            
            messages.error(request, 'Invalid username or password.')

    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    return redirect('/login')

def home(request):
    return render(request, 'core/home.html', {})


# Course page view (requires login)

@login_required(login_url='/login')
def course_page(request):
    modules = Module.objects.prefetch_related('lessons').all()
    
    context = {
        'modules': modules
    }
    
    return render(request, 'core/course-content-page.html', context)


# Creating a Module
def create_module(request):
    form =  ModuleForm()
    
    if request.method == 'POST':
        form =  ModuleForm(
            request.POST, request.FILES
        )
        
        if form.is_valid():
            form.save()
            return redirect('course-page')
        else:
            form =  ModuleForm()
            
            
    return render(request, 'core/create-module.html', {'form':form})


def add_lesson(request):
    form =  LessonForm()
    
    if request.method == 'POST':
        form =  LessonForm(
            request.POST, request.FILES
        )
        
        if form.is_valid():
            form.save()
            return redirect('course-page')
        else:
            form =  LessonForm()
            
            
    return render(request, 'core/addLesson.html', {'form':form})

def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, id=pk)
    modules = Module.objects.prefetch_related('lessons').all()
    
    context = {
        'lesson': lesson,
        'modules': modules
    }

    return render(request, 'core/lesson-details.html', context)



