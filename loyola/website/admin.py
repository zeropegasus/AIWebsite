from django.contrib import admin
from .models import Program, Module, Workshop, Lab, Assignment, Submission, Instructor, Student

# Register your models here.

class ProgramAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "description")

class ModuleAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "description")

class WorkshopAdmin(admin.ModelAdmin):
    list_display = ("title", "order")

class LabAdmin(admin.ModelAdmin):
    list_display = ("title", "description")

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ("title", "description")

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("feedback", "score")

class InstructorAdmin(admin.ModelAdmin):
    list_display = ("name", "id")

class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "id")

admin.site.register(Program, ProgramAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Lab, LabAdmin)
admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Student, StudentAdmin)
