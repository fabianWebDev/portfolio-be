from django.urls import path
from .views import ProjectListView, ProjectDetailView

app_name = 'projects_api'

urlpatterns = [
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
]
