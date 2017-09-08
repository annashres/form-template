"""
Definition of forms.
"""

from django import forms
from django.forms import ModelForm, Textarea, SelectMultiple
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

from django.forms.extras.widgets import SelectDateWidget
from datetimewidget.widgets import DateWidget
from .models import *
