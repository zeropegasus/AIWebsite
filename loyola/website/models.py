from django.db import models

"""
    Foreign key single vs. many:
        models.ManyToManyField
        models.ForeignKey
        
    Referencing models that are declared later:
        https://stackoverflow.com/questions/41311070/django-use-a-model-before-its-definition-in-another-model
    
    3-22:
        Added Program, Workshop, Instructor, Student
        Updated foreign keys for most models
"""

from ckeditor_uploader.fields import RichTextUploadingField

class Program(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True) 
    # description = models.TextField(null=True, blank=True)
    description = RichTextUploadingField(null=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    # image = models.ImageField(null=True, blank=True)
    image = models.ImageField(upload_to='website/static/img/program/', default='default.jpg')
    category = models.CharField(max_length=255, null=True, blank=True)
    is_published = models.BooleanField(null=True, blank=True)
    this_prerequisites = models.ManyToManyField("self", null=True, blank=True)
    # symmetrical = False, blank=True, null=True
    this_modules = models.ManyToManyField("Module", null=True, blank=True)
    this_assignments = models.ManyToManyField("Assignment", null=True, blank=True)
    this_students = models.ManyToManyField("Student", null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

class Module(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='website/static/img/module/', default='default.jpg')
    category = models.CharField(max_length=255, null=True, blank=True)
    is_published = models.BooleanField(null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    files = models.FileField(null=True, blank=True)
    this_workshops = models.ManyToManyField("Workshop", null=True, blank=True)
    this_program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"
    
class Workshop(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='website/static/img/workshop/', default='default.jpg')
    category = models.CharField(max_length=255, null=True, blank=True)
    is_published = models.BooleanField(null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    files = models.FileField(null=True, blank=True)
    this_lab = models.ForeignKey("Lab", on_delete=models.CASCADE, null=True, blank=True)
    this_instructors = models.ManyToManyField("Instructor", null=True, blank=True)
    this_module = models.ForeignKey(Module, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

class Lab(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    this_module = models.ForeignKey(Module, on_delete=models.CASCADE, null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)
    instructions = models.TextField(null=True, blank=True)
    materials = models.TextField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField(null=True, blank=True)
    files = models.FileField(null=True, blank=True)
    this_workshop = models.ForeignKey("Workshop", on_delete=models.CASCADE, null=True, blank=True)
    this_instructors = models.ManyToManyField("Instructor", null=True, blank=True)
    this_assignment = models.ManyToManyField("Assignment", null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

class Assignment(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    instructions = models.TextField(null=True, blank=True)
    max_score = models.IntegerField(null=True, blank=True)
    is_published = models.BooleanField(null=True, blank=True)
    files = models.FileField(null=True, blank=True)
    this_program = models.ForeignKey("Program", on_delete=models.CASCADE, null=True, blank=True)
    this_submissions = models.ManyToManyField("Submission", null=True, blank=True)
    this_lab = models.ForeignKey("Lab", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

class Submission(models.Model):
    submission_date = models.DateTimeField(null=True, blank=True)
    files = models.FileField(null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)
    this_student = models.ForeignKey("Student", on_delete=models.CASCADE, null=True, blank=True)
    this_assignment = models.ForeignKey("Assignment", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.id}"

class Instructor(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    affiliation = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='website/static/img/instructor/', default='default.jpg')
    this_workshops = models.ManyToManyField("Workshop", null=True, blank=True)
    this_labs = models.ManyToManyField("Lab", null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
    
class Student(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    this_program = models.ForeignKey("Program", on_delete=models.CASCADE, null=True, blank=True)
    this_submissions = models.ManyToManyField("Submission", null=True, blank=True)

    def __str__(self):
        return f"{self.name}"