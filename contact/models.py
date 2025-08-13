from django.db import models
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.

class ContactMessage(models.Model):
    """
    Model to represent contact messages from visitors.
    Stores contact information and messages sent through the contact form.
    """
    
    # Main fields
    name = models.CharField(
        max_length=100,
        verbose_name="Name",
        help_text="Full name of the person sending the message (maximum 100 characters)"
    )
    
    email = models.EmailField(
        verbose_name="Email address",
        help_text="Email address for contact",
        validators=[EmailValidator()]
    )
    
    message = models.TextField(
        verbose_name="Message",
        help_text="Content of the contact message"
    )

    # Status fields
    is_read = models.BooleanField(
        default=False,
        verbose_name="Read",
        help_text="Indicates if the message has been read"
    )
    
    is_responded = models.BooleanField(
        default=False,
        verbose_name="Responded",
        help_text="Indicates if a response has been sent"
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
    
    read_at = models.DateTimeField(
        verbose_name="Read at",
        help_text="When the message was first read",
        blank=True,
        null=True
    )
    
    responded_at = models.DateTimeField(
        verbose_name="Responded at",
        help_text="When the response was sent",
        blank=True,
        null=True
    )
    
    # Meta information
    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
        ordering = ['-created_at']
        db_table = 'contact_messages'
    
    def __str__(self):
        return f"Message from {self.name} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
    
    def clean(self):
        """Custom model validation"""
        super().clean()
        
        # Validate that email is provided
        if not self.email:
            raise ValidationError(
                "You must provide an email address"
            )
    
    def mark_as_read(self):
        """Mark the message as read"""
        if not self.is_read:
            self.is_read = True
            self.read_at = timezone.now()
            self.save(update_fields=['is_read', 'read_at'])
    
    def mark_as_responded(self):
        """Mark the message as responded"""
        if not self.is_responded:
            self.is_responded = True
            self.responded_at = timezone.now()
            self.save(update_fields=['is_responded', 'responded_at'])
    
    @property
    def display_name(self):
        """Returns the display name"""
        return self.name
    
    @property
    def contact_info(self):
        """Returns the primary contact information"""
        return self.email
    
    @property
    def is_new(self):
        """Returns True if the message is unread"""
        return not self.is_read
    
    @property
    def needs_response(self):
        """Returns True if the message needs a response"""
        return not self.is_responded
    
    def save(self, *args, **kwargs):
        """Override save method for additional validations"""
        self.full_clean()
        super().save(*args, **kwargs)
