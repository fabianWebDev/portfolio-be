from rest_framework import serializers
from projects.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer for the Project model.
    Provides full representation of project data for API responses.
    """

    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'display_name',
            'image',
            'description',
            'short_description',
            'link',
            'github_url',
            'techs_used',
            'tech_list',
            'is_active',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class ProjectListSerializer(serializers.ModelSerializer):
    """
    Simplified serializer for project list view.
    Includes only essential fields for listing projects.
    """

    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'image',
            'short_description',
            'tech_list',
            'link',
            'github_url',
            'is_active',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at']
