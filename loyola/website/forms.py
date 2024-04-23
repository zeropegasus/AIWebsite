from django import forms
from .models import Program, Module, Workshop, Lab, Assignment, Instructor, Submission, Student

from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ProgramsForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = [
            "title",
            "description",
            "start_date",
            "end_date",
            "created_at",
            "updated_at",
            "duration",
            "image",
            "category",
            "is_published",
            "this_prerequisites",
            "this_modules",
            "this_assignments",
            "this_students",
        ]
    widgets = {
        "title": forms.TextInput(attrs={'class': 'p'}),
        # "description": forms.TextInput(attrs={'class': 'p'}),
        "description": forms.CharField(widget=CKEditorUploadingWidget(attrs={'class': 'p'})),
        "start_date": forms.DateInput(attrs={'class': 'p'}),
        "end_date": forms.DateInput(attrs={'class': 'p'}),
        "created_at": forms.TimeInput(attrs={'type': 'time'}),
        "updated_at": forms.TimeInput(attrs={'type': 'time'}),
        "duration": forms.NumberInput(attrs={'class': 'p'}),  # Integer input
        "image": forms.TextInput(attrs={'class': 'p'}),  # Assuming image URL is text input
        "category": forms.TextInput(attrs={'class': 'p'}),
        "is_published": forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'p'})),  # Boolean input
        "this_prerequisites": forms.TextInput(attrs={'class': 'p'}),
        "this_modules": forms.TextInput(attrs={'class': 'p'}),
        "this_assignments": forms.TextInput(attrs={'class': 'p'}),
        "this_students": forms.TextInput(attrs={'class': 'p'}),
    }

class ModulesForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = [
            "title",
            "description",
            "duration",
            "image",
            "category",
            "is_published",
            "order",
            "notes",
            "files",
            "this_workshops",
            "this_program",
        ]

    # Add CSS classes to the widget attributes
    widgets = {
        "title": forms.TextInput(attrs={'class': 'p'}),
        "description": forms.TextInput(attrs={'class': 'p'}),
        "duration": forms.NumberInput(attrs={'class': 'p'}),  # Integer input
        "image": forms.TextInput(attrs={'class': 'p'}),  # Assuming image URL is text input
        "category": forms.TextInput(attrs={'class': 'p'}),
        "is_published": forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'p'})),  # Boolean input
        "order": forms.NumberInput(attrs={'class': 'p'}),  # Integer input
        "notes": forms.TextInput(attrs={'class': 'p'}),
        "files": forms.TextInput(attrs={'class': 'p'}),  # Assuming file URL is text input
        "this_workshops": forms.TextInput(attrs={'class': 'p'}),
        "this_program": forms.TextInput(attrs={'class': 'p'}),
    }

class WorkshopsForm(forms.ModelForm):
    class Meta:
        model = Workshop
        fields = [
            "title",
            "description",
            "duration",
            "image",
            "category",
            "is_published",
            "order",
            "notes",
            "files",
            "this_lab",
            "this_instructors",
            "this_module",
        ]

    widgets = {
        "title": forms.TextInput(attrs={'class': 'p'}),
        "description": forms.TextInput(attrs={'class': 'p'}),
        "duration": forms.NumberInput(attrs={'class': 'p'}),  # Integer input
        "image": forms.TextInput(attrs={'class': 'p'}),  # Assuming image URL is text input
        "category": forms.TextInput(attrs={'class': 'p'}),
        "is_published": forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'p'})),  # Boolean input
        "order": forms.NumberInput(attrs={'class': 'p'}),  # Integer input
        "notes": forms.TextInput(attrs={'class': 'p'}),
        "files": forms.TextInput(attrs={'class': 'p'}),  # Assuming file URL is text input
        "this_lab": forms.TextInput(attrs={'class': 'p'}),
        "this_instructors": forms.TextInput(attrs={'class': 'p'}),
        "this_program": forms.TextInput(attrs={'class': 'p'}),
    }

class LabsForm(forms.ModelForm):
    class Meta:
        model = Lab
        fields = [
            "title",
            "description",
            "this_module",
            "order",
            "instructions",
            "materials",
            "due_date",
            "is_completed",
            "files",
            "this_workshop",
            "this_instructors",
            "this_assignment",
        ]

    # Add CSS classes to the widget attributes
    widgets = {
        "title": forms.TextInput(attrs={'class': 'p'}),
        "description": forms.TextInput(attrs={'class': 'p'}),
        "this_module": forms.TextInput(attrs={'class': 'p'}),
        "order": forms.NumberInput(attrs={'class': 'p'}),
        "instructions": forms.TextInput(attrs={'class': 'p'}),
        "materials": forms.TextInput(attrs={'class': 'p'}),
        "due_date": forms.DateInput(attrs={'class': 'p'}),
        "is_completed": forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'p'})),  # Boolean input
        "files": forms.TextInput(attrs={'class': 'p'}),
        "this_workshop": forms.TextInput(attrs={'class': 'p'}),
        "this_instructors": forms.TextInput(attrs={'class': 'p'}),
        "this_assignment": forms.TextInput(attrs={'class': 'p'}),
    }

class AssignmentsForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = '__all__'

    widgets = {
        "title": forms.TextInput(attrs={'class': 'p'}),
        "description": forms.TextInput(attrs={'class': 'p'}),
        "due_date": forms.DateInput(attrs={'class': 'p'}),
        "instructions": forms.TextInput(attrs={'class': 'p'}),
        "max_score": forms.NumberInput(attrs={'class': 'p'}),
        "is_published": forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'p'})),
        "files": forms.TextInput(attrs={'class': 'p'}),
        "this_program": forms.TextInput(attrs={'class': 'p'}),
        "this_submissions": forms.TextInput(attrs={'class': 'p'}),
        "this_lab": forms.TextInput(attrs={'class': 'p'}),
    }

class SubmissionsForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = '__all__'
    
    widgets = {
        "submission_date": forms.DateInput(attrs={'class': 'p'}),
        "files": forms.TextInput(attrs={'class': 'p'}),
        "feedback": forms.TextInput(attrs={'class': 'p'}),
        "score": forms.NumberInput(attrs={'class': 'p'}),
        "this_student": forms.TextInput(attrs={'class': 'p'}),
        "this_assignment": forms.TextInput(attrs={'class': 'p'}),
    }

class InstructorsForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = '__all__'

    widgets = {
        "name": forms.TextInput(attrs={'class': 'p'}),
        "description": forms.TextInput(attrs={'class': 'p'}),
        "picture": forms.TextInput(attrs={'class': 'p'}),
        "this_workshops": forms.TextInput(attrs={'class': 'p'}),
        "this_labs": forms.TextInput(attrs={'class': 'p'}),
    }

