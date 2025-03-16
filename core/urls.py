from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('course_page/', views.course_page, name='course-page'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'), 
    path('Add_content/', views.Add_content, name='Add-content'),

]
