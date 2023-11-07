from django.views.generic import TemplateView
from accounts.models import CustomUser, Project, SupervisorRequest
from django.shortcuts import redirect, render, get_object_or_404
from .forms import ProjectForm, SupervisorRequestForm
from django.http import HttpResponse


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"


def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            # Save the project to the database
            project = form.save(commit=False)
            project.submitted_request = True  # You can set other fields as needed
            project.save()
            # Perform any other actions or redirection here
            return redirect('project_submitted', project_id=project.id)
    else:
        form = ProjectForm()

    return render(request, 'pages/create_project.html', {'form': form})


def project_submitted(request, project_id):
    # Retrieve the project based on the provided project_id
    project = Project.objects.get(id=project_id)
    return render(request, 'pages/project_submitted.html', {'project': project})


def projects_list(request):
    projects = Project.objects.all()
    return render(request, 'pages/project_list.html', {'projects': projects})

  # Create a form for supervisor requests


def create_supervisor_request(request, project_id):
    # Assuming the user is the student making the request
    student = request.user

    # Check if the project exists
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        # Handle project not found (e.g., redirect to an error page)
        return HttpResponse('project_not_found')

    if request.method == 'POST':
        form = SupervisorRequestForm(request.POST)
        if form.is_valid():
            # Create and save the supervisor request
            user_form = form.save(commit=False)
            user_form.student = student
            user_form.project = project
            user_form.save()

            # Redirect to a success page or project details page
            return redirect('projects_list')
    else:
        form = SupervisorRequestForm()

    return render(request, 'pages/request_supervisor.html', {'form': form, 'project': project})
