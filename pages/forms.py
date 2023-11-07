from django import forms
from accounts.models import CustomUser, Project, SupervisorRequest
from django.contrib.auth.forms import UserCreationForm


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', ]


class SupervisorRequestForm(forms.ModelForm):
    class Meta:
        model = SupervisorRequest
        fields = ['request_text']


class SuperuserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email',)
