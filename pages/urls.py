from django.urls import path

from .views import (HomePageView, create_project, superuser_signup, delete_project, edit_project,
                    project_submitted, projects_list, create_supervisor_request)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("create-project/", create_project, name="create_project"),
    path('project_submitted/<int:project_id>/',
         project_submitted, name='project_submitted'),
    path('projects_list/', projects_list, name='projects_list'),
    path('create_supervisor_request/<int:project_id>/',
         create_supervisor_request, name='create_supervisor_request'),
    path('delete_project/<int:project_id>/',
         delete_project, name='delete_project'),
     path('edit_project/<int:project_id>/', edit_project, name='edit_project'),

    # Accounts
    path('superuser/signup/', superuser_signup, name='superuser_signup'),

]
