from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('course_page/', views.course_page, name='course-page')
]
