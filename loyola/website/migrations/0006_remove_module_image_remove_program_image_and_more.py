# Generated by Django 5.0.1 on 2024-04-23 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_remove_instructor_picture_instructor_affiliation_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='image',
        ),
        migrations.RemoveField(
            model_name='program',
            name='image',
        ),
        migrations.RemoveField(
            model_name='workshop',
            name='image',
        ),
    ]
