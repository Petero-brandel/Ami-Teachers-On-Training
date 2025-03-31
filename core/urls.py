from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('course_page/', views.course_page, name='course-page'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'), 
    path('create-module/', views.create_module, name='create-module'),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

