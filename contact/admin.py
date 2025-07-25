from django.contrib import admin
from .models import ContactMessage

# Register your models here.


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """
    Admin configuration for ContactMessage model.
    Provides a comprehensive interface for managing contact messages.
    """

    # Fields to display in the list view
    list_display = [
        'name',
        'email',
        'phone',
        'subject',
        'is_read',
        'is_responded',
        'created_at'
    ]

    # Fields to filter by
    list_filter = [
        'is_read',
        'is_responded',
        'created_at',
        'updated_at'
    ]

    # Fields to search in
    search_fields = [
        'name',
        'email',
        'phone',
        'subject',
        'message'
    ]

    # Fields to display in the detail view
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Message Content', {
            'fields': ('subject', 'message')
        }),
        ('Status', {
            'fields': ('is_read', 'is_responded', 'read_at', 'responded_at'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )

    # Read-only fields
    readonly_fields = [
        'created_at',
        'updated_at',
        'read_at',
        'responded_at'
    ]

    # Actions
    actions = ['mark_as_read', 'mark_as_responded']

    # Ordering
    ordering = ['-created_at']

    # Items per page
    list_per_page = 25

    # Date hierarchy
    date_hierarchy = 'created_at'

    def mark_as_read(self, request, queryset):
        """Action to mark selected messages as read"""
        updated = queryset.update(is_read=True)
        self.message_user(
            request,
            f'{updated} message(s) marked as read.'
        )
    mark_as_read.short_description = "Mark selected messages as read"

    def mark_as_responded(self, request, queryset):
        """Action to mark selected messages as responded"""
        updated = queryset.update(is_responded=True)
        self.message_user(
            request,
            f'{updated} message(s) marked as responded.'
        )
    mark_as_responded.short_description = "Mark selected messages as responded"

    def get_queryset(self, request):
        """Custom queryset with annotations"""
        return super().get_queryset(request)

    def has_add_permission(self, request):
        """Disable adding messages from admin (they should come from the form)"""
        return False
