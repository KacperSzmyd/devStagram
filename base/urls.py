from django.urls import path

from .views import ProjectListView, ProjectView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView

urlpatterns = [
    path('', ProjectListView.as_view(), name='projects'),
    path('project/<uuid:pk>/', ProjectView.as_view(), name='project'),
    path('project-create/', ProjectCreateView.as_view(), name='project-create'),
    path('project/<uuid:pk>/edit/', ProjectUpdateView.as_view(), name='project-edit'),
    path('project/<uuid:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
]