from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from projects.models import Project
from .serializers import ProjectSerializer, ProjectListSerializer


class ProjectListView(generics.ListAPIView):
    """
    API view for listing all active projects.
    Returns a simplified list of projects with essential information.
    """
    serializer_class = ProjectListSerializer
    queryset = Project.objects.filter(is_active=True)
    
    def get_queryset(self):
        """
        Return only active projects, ordered by creation date (newest first).
        """
        return Project.objects.filter(is_active=True).order_by('-created_at')


class ProjectDetailView(generics.RetrieveAPIView):
    """
    API view for retrieving detailed information about a specific project.
    Returns complete project information including full description and metadata.
    """
    serializer_class = ProjectSerializer
    queryset = Project.objects.filter(is_active=True)
    lookup_field = 'pk'
    
    def get_object(self):
        """
        Get the project object or return 404 if not found or inactive.
        """
        pk = self.kwargs.get('pk')
        return get_object_or_404(Project, pk=pk, is_active=True)
