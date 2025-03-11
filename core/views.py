from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomSignupForm, UpdateCourseForm  # Import your custom form
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



def sign_up(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home') 
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

@login_required
def course_page(request):
    return render(request, 'core/course-content-page.html', {})

def update_course(request):
    form = UpdateCourseForm()
    
    if request.method == 'POST':
    
        form = UpdateCourseForm(request.post)
        if form.is_valid():
            form.save()
            return redirect('course-page')
        else:
            form = UpdateCourseForm()
    
    return render(request, 'core/update-course.html', {'form': form})