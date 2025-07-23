from django.db import models
from django.utils import timezone
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

# Create your models here.

class Project(models.Model):
    """
    Model to represent projects in the portfolio.
    Includes basic project information, technologies used and metadata.
    """
    
    # Main fields
    name = models.CharField(
        max_length=200,
        verbose_name="Project name",
        help_text="Name of the project (maximum 200 characters)"
    )
    
    image = models.ImageField(
        upload_to='projects/images/',
        verbose_name="Project image",
        help_text="Representative image of the project",
        blank=True,
        null=True
    )
    
    description = models.TextField(
        verbose_name="Description",
        help_text="Detailed description of the project"
    )
    
    link = models.URLField(
        verbose_name="Project link",
        help_text="URL of the project (GitHub, demo, etc.)",
        blank=True,
        null=True,
        validators=[URLValidator()]
    )
    
    # Field for technologies (as text, but you could create a separate model)
    techs_used = models.TextField(
        verbose_name="Technologies used",
        help_text="List of technologies, frameworks and tools used",
        blank=True
    )
    
    # Additional recommended fields
    short_description = models.CharField(
        max_length=300,
        verbose_name="Short description",
        help_text="Brief description of the project (maximum 300 characters)",
        blank=True
    )
    
    github_url = models.URLField(
        verbose_name="GitHub URL",
        help_text="Link to the GitHub repository",
        blank=True,
        null=True,
        validators=[URLValidator()]
    )
    
    # Status and ordering fields
    is_active = models.BooleanField(
        default=True,
        verbose_name="Active",
        help_text="Indicates if the project is active and visible"
    )
    
    # Date fields
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created at"
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated at"
    )
    
    # Meta information
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ['-created_at']
        db_table = 'projects'
    
    def __str__(self):
        return self.name
    
    def clean(self):
        """Custom model validation"""
        super().clean()
        
        # Validate that at least one link is present
        if not self.link and not self.github_url:
            raise ValidationError(
                "You must provide at least one link (link or GitHub)"
            )
    
    def get_absolute_url(self):
        """Returns the absolute URL of the project"""
        from django.urls import reverse
        return reverse('projects:detail', kwargs={'pk': self.pk})
    
    @property
    def display_name(self):
        """Returns the display name"""
        return self.name
    
    @property
    def tech_list(self):
        """Returns technologies as a list"""
        if self.techs_used:
            return [tech.strip() for tech in self.techs_used.split(',') if tech.strip()]
        return []
    
    def save(self, *args, **kwargs):
        """Override save method for additional validations"""
        self.full_clean()
        super().save(*args, **kwargs)
