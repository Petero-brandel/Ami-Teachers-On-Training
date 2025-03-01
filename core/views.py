from django.shortcuts import render


# Create your views here.
def home(request):
    
    return render(request, 'core/home.html', {})

def course_page(request):
    
    return render(request, 'core/course-content-page.html', {})