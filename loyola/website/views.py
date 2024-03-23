from django.http import HttpResponse
from django.template import loader
from .models import Program, Module, Workshop, Lab, Assignment, Submission, Instructor, Student

def education(request):
    myModules = Module.objects.all().values()
    myLabs = Lab.objects.all().values()
    mySubmissions = Submission.objects.all().values()
    myAssignments = Assignment.objects.all().values()

    context = {
        'myModules': myModules,
        'myLabs': myLabs,
        'mySubmissions': mySubmissions,
        'myAssignments': myAssignments
    }
    template = loader.get_template('main.html')
    return HttpResponse(template.render(context, request))