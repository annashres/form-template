"""
Definition of views.
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.db import connection
from django.template.loader import render_to_string
from .models import *
from .forms import *

def register(request):
    if request.method == "POST":
        form = FORM_NAME(request.POST)
        if form.is_valid():
            reg = form.save()
            return redirect('done')
    else:
        form = FORM_NAME()
    return render(request, 'app/form.html', {'form': form})


def done(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/done.html',
    )