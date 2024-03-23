from django.shortcuts import HttpResponse, render
from django.template import loader
from .models import Program, Module, Workshop, Lab, Assignment, Submission, Instructor, Student

def education(request):
    myPrograms = Program.objects.all().values()
    myModules = Module.objects.all().values()
    myLabs = Lab.objects.all().values()
    mySubmissions = Submission.objects.all().values()
    myAssignments = Assignment.objects.all().values()

    context = {
        'myPrograms': myPrograms,
        'myModules': myModules,
        'myLabs': myLabs,
        'mySubmissions': mySubmissions,
        'myAssignments': myAssignments
    }
    return render(request, "main.html", context)


def program_detail_view(request, id):
    # Select program based on its id
    program = Program.objects.get(id = id)
    
    context = {
        'program': program
    }

    return render(request, "program.html", context)

def module_detail_view(request, order):
    # Select module based on its order
    module = Module.objects.get(order = order)
    
    context = {
        'module': module
    }

    return render(request, "module.html", context)

def workshop_detail_view(request, order):
    # Select workshop based on its order
    workshop = Workshop.objects.get(order = order)
    lab = workshop.this_lab
    
    context = {
        'workshop': workshop,
        'lab': lab
    }

    return render(request, "workshop.html", context)