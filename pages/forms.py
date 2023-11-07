from django import forms
from accounts.models import CustomUser, Project, SupervisorRequest
from django.forms.widgets import RadioSelect


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', ]


class SupervisorRequestForm(forms.ModelForm):
    class Meta:
        model = SupervisorRequest
        fields = ['request_text']
