from django.http import HttpResponse
from django.template import loader
from .models import Course, Module, Lab, Submission, Assignment
from django.shortcuts import render, get_object_or_404

def education(request):
    myCourses = Course.objects.all().values()
    myModules = Module.objects.all().values()
    myLabs = Lab.objects.all().values()
    mySubmissions = Submission.objects.all().values()
    myAssignments = Assignment.objects.all().values()

    context = {
        'myCourses': myCourses,
        'myModules': myModules,
        'myLabs': myLabs,
        'mySubmissions': mySubmissions,
        'myAssignments': myAssignments
    }
    template = loader.get_template('main.html')
    return HttpResponse(template.render(context, request))

def course_detail(request, pk):
    # Retrieve the specific Course object from the database
    course = get_object_or_404(Course, pk=pk)
    
    # Render the template with the retrieved object
    return render(request, 'course_detail.html', {'myCourses': Course})

def module_detail(request, pk):
    # Retrieve the specific Course object from the database
    module = get_object_or_404(Module, pk=pk)
    
    # Render the template with the retrieved object
    return render(request, 'module_detail.html', {'myModules': Module})

def lab_detail(request, pk):
    # Retrieve the specific Course object from the database
    lab = get_object_or_404(Lab, pk=pk)
    
    # Render the template with the retrieved object
    return render(request, 'lab_detail.html', {'myLabs': Lab})

def submission_detail(request, pk):
    # Retrieve the specific Course object from the database
    course = get_object_or_404(Submission, pk=pk)
    
    # Render the template with the retrieved object
    return render(request, 'submission_detail.html', {'mySubmissions': Submission})

def assignment_detail(request, pk):
    # Retrieve the specific Course object from the database
    course = get_object_or_404(Assignment, pk=pk)
    
    # Render the template with the retrieved object
    return render(request, 'assignment_detail.html', {'myAssignments': Assignment})