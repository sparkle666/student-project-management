from django.urls import path

from .views import (HomePageView, create_project, superuser_signup,
                    project_submitted, projects_list, create_supervisor_request)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("create-project/", create_project, name="create_project"),
    path('project_submitted/<int:project_id>/',
         project_submitted, name='project_submitted'),
    path('projects_list/', projects_list, name='projects_list'),
    path('create_supervisor_request/<int:project_id>/',
         create_supervisor_request, name='create_supervisor_request'),
    path('superuser/signup/', superuser_signup, name='superuser_signup'),

]
