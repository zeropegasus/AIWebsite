from django.shortcuts import HttpResponseRedirect, render, get_object_or_404
from django.template import loader
from .models import Program, Module, Workshop, Lab, Assignment, Submission, Instructor, Student

from .forms import ProgramsForm, ModulesForm, WorkshopsForm, LabsForm

    # myPrograms = Program.objects.all().values()
    # myModules = Module.objects.all().values()
    # myLabs = Lab.objects.all().values()
    # mySubmissions = Submission.objects.all().values()
    # myAssignments = Assignment.objects.all().values()


def program_detail_view(request, id):
    # Select program based on its id
    program = Program.objects.get(id = id)
    
    # Template uses context to reference db entries
    context = {
        'program': program
    }

    # Render program template, using context dict
    return render(request, "program.html", context)

def program_create_view(request):
    context = {}

    form = ProgramsForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # Save form data to model
        form.save()
        return HttpResponseRedirect("/program/1")
    
    context['form'] = form
    return render(request, "crud/program_create.html", context)

def program_update_delete_view(request, id):
    program = Program.objects.get(id = id)
    context = {
        'program': program
    }
    obj = get_object_or_404(Program, id=id)

    if request.method == "POST":
        # Check if the form was submitted for update
        if 'update' in request.POST:
            form = ProgramsForm(request.POST or None, request.FILES or None, instance=obj)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/program/1")

        # Check if the form was submitted for delete
        if 'delete' in request.POST:
            obj.delete()
            return HttpResponseRedirect("/program/1")

    else:
        form = ProgramsForm(instance=obj)

    context["form"] = form
    context["id"] = id

    return render(request, "crud/program_update_delete.html", context)

def module_detail_view(request, order):
    # Select module based on its order
    module = Module.objects.get(order = order)
    
    # Template uses context to reference db entries
    context = {
        'module': module
    }

    # Render module template, using context dict
    return render(request, "moduledetail.html", context)

def module_create_view(request):
    context = {}

    form = ModulesForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # Save form data to model
        form.save()
        return HttpResponseRedirect("/program/1")
    
    context['form'] = form
    return render(request, "crud/module_create.html", context)

def module_update_delete_view(request, order):
    module = Module.objects.get(order = order)
    context = {
        'module': module
    }
    obj = get_object_or_404(Module, order=order)

    if request.method == "POST":
        # Check if the form was submitted for update
        if 'update' in request.POST:
            form = ModulesForm(request.POST or None, request.FILES or None, instance=obj)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/program/1")

        # Check if the form was submitted for delete
        if 'delete' in request.POST:
            obj.delete()
            return HttpResponseRedirect("/program/1")

    else:
        form = ModulesForm(instance=obj)

    context["form"] = form
    context["order"] = order

    return render(request, "crud/module_update_delete.html", context)


def workshop_detail_view(request, order):
    # Select workshop based on its order
    workshop = Workshop.objects.get(order = order)
    # Easier to reference lab within template
    lab = workshop.this_lab
    
    # Template uses context to reference db entries
    context = {
        'workshop': workshop,
        'lab': lab
    }

    # Render workshop template, using context dict
    return render(request, "workshopdetail.html", context)

def workshop_create_view(request):
    context = {}

    form = WorkshopsForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # Save form data to model
        form.save()
        return HttpResponseRedirect("/program/1")
    
    context['form'] = form
    return render(request, "crud/workshop_create.html", context)

def workshop_update_delete_view(request, order):
    workshop = Workshop.objects.get(order = order)
    context = {
        'workshop': workshop
    }
    obj = get_object_or_404(Workshop, order=order)

    if request.method == "POST":
        # Check if the form was submitted for update
        if 'update' in request.POST:
            form = WorkshopsForm(request.POST or None, request.FILES or None, instance=obj)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/program/1")

        # Check if the form was submitted for delete
        if 'delete' in request.POST:
            obj.delete()
            return HttpResponseRedirect("/program/1")

    else:
        form = WorkshopsForm(instance=obj)

    context["form"] = form
    context["order"] = order

    return render(request, "crud/workshop_update_delete.html", context)   

def lab_list_view(request):
    # Select lab based on its order
    labs = Lab.objects.all().values()
    # Template uses context to reference db entries
    context = {
        'labs': labs
    }

    # Render module template, using context dict
    return render(request, "lablist.html", context)

def lab_detail_view(request, order):
    # Select program based on its id
    lab = Lab.objects.get(order = order)
    
    # Template uses context to reference db entries
    context = {
        'lab': lab
    }

    # Render program template, using context dict
    return render(request, "labdetail.html", context)

def lab_create_view(request):
    context = {}

    form = LabsForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # Save form data to model
        form.save()
        return HttpResponseRedirect("/program/1")
    
    context['form'] = form
    return render(request, "crud/lab_create.html", context)

def lab_update_delete_view(request, order):
    context = {}

    obj = get_object_or_404(Lab, order=order)

    if request.method == "POST":
        # Check if the form was submitted for update
        if 'update' in request.POST:
            form = LabsForm(request.POST or None, request.FILES or None, instance=obj)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/program/1")

        # Check if the form was submitted for delete
        if 'delete' in request.POST:
            obj.delete()
            return HttpResponseRedirect("/program/1")

    else:
        form = LabsForm(instance=obj)

    context["form"] = form
    context["order"] = order

    return render(request, "crud/lab_update_delete.html", context)  
