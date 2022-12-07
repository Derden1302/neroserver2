from django import forms
from .models import *
from django.contrib.postgres.forms.array import SimpleArrayField


class ResponseGraphic(forms.Form):
    graphicview = models.CharField()
    items = models.CharField()
    type = models.CharField()
    range = models.IntegerField()
    period = models.IntegerField()
