# Generated by Django 4.2.4 on 2024-03-23 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_instructor_program_student_workshop_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
