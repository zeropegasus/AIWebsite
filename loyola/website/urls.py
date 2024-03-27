from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('program/<int:id>/', views.program_detail_view, name='program_detail_view'),
    path('module/<int:order>/', views.module_detail_view, name='module_detail_view'),
    path('workshop/<int:order>/', views.workshop_detail_view, name='workshop_detail_view')

]