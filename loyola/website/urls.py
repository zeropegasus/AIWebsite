from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('program/<int:id>', views.program_detail_view, name='program_detail_view'),
    path('module/<int:order>', views.module_detail_view, name='module_detail_view'),
    path('workshop/<int:order>', views.workshop_detail_view, name='program_detail_view'),
    path('program/create', views.program_create_view, name='module_create_view'),
    path('program/<int:id>/update_delete', views.program_update_delete_view, name='program_update_delete_view'),
    path('module/create', views.module_create_view, name='module_create_view'),
    path('module/<int:order>/update_delete', views.module_update_delete_view, name='module_update_delete_view'),
    path('workshop/create', views.workshop_create_view, name='workshop_create_view'),
    path('workshop/<int:order>/update_delete', views.workshop_update_delete_view, name='workshop_update_delete_view'),
    path('lab/create', views.lab_create_view, name='lab_create_view'),
    path('lab/<int:order>/update_delete', views.lab_update_delete_view, name='lab_update_delete_view'),
]