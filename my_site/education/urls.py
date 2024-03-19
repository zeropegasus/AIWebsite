from django.urls import path
from . import views
from .views import course_detail, assignment_detail, lab_detail, module_detail, submission_detail

urlpatterns = [
    path('', views.education, name='education'),
    path('education/', views.education, name='education'),
    path('course/<int:pk>/', course_detail, name='course_detail'),
    path('assignment/<int:pk>/', assignment_detail, name='assignment_detail'),
    path('lab/<int:pk>/', lab_detail, name='lab_detail'),
    path('module/<int:pk>/', module_detail, name='module_detail'),
    
]

