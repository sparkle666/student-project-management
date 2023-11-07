from django.views.generic import TemplateView
from accounts.models import CustomUser, Project, SupervisorRequest
from django.shortcuts import redirect, render, get_object_or_404
from .forms import ProjectForm, SuperuserCreationForm, SupervisorRequestForm
from django.http import HttpResponse
from django.contrib import auth
from django.urls import reverse
from django.contrib import messages


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
            project.student = request.user
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
    projects = Project.objects.filter(student=request.user)

    context = {'projects': projects}
    # if not projects.exists():
    #     context = {'projects': []}

    return render(request, 'pages/project_list.html', context)

  # Create a form for supervisor requests


def delete_project(request, project_id):
    try:
        project = Project.objects.get(pk=project_id)
        project.delete()
    except Project.DoesNotExist:
        messages.error(
            request, 'The project does not exist or has already been deleted.')

    return redirect('projects_list')


def edit_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects_list')
    else:
        form = ProjectForm(instance=project)

    return render(request, 'pages/edit_project.html', {'form': form, 'project': project})


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


def superuser_signup(request):
    if request.method == 'POST':
        form = SuperuserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_superuser = True
            user.is_staff = True
            user.save()

            # Log in the superuser
            user = auth.authenticate(
                username=user.username, password=request.POST['password1'])
            if user is not None:
                auth.login(request, user)

            # Redirect to the admin dashboard.
            return redirect(reverse('admin:index'))
    else:
        form = SuperuserCreationForm()
    return render(request, 'account/superuser_signup.html', {'form': form})
