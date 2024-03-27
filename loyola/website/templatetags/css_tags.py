# css_tags.py

from django import template
from django.templatetags.static import static
import os

register = template.Library()

@register.simple_tag
def include_css_files(*files):
    css_links = ''
    for file in files:
        # Assuming 'staticfiles' is the directory where your static files are collected
        static_file_path = os.path.join('staticfiles', file)
        css_links += f'<link rel="stylesheet" href="{static(static_file_path)}">'
    return css_links
