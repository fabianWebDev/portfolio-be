from rest_framework import serializers
from contact.models import ContactMessage


class ContactMessageCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating new contact messages.
    Includes only the fields needed for creating a new message.
    """
    
    class Meta:
        model = ContactMessage
        fields = [
            'name',
            'email',
            'message',
        ]
    
    def validate(self, data):
        """
        Custom validation to ensure email is provided.
        """
        email = data.get('email')
        
        if not email:
            raise serializers.ValidationError(
                "You must provide an email address"
            )
        
        return data
    
    def create(self, validated_data):
        """
        Create a new contact message.
        """
        return ContactMessage.objects.create(**validated_data)


class ContactMessageResponseSerializer(serializers.ModelSerializer):
    """
    Serializer for API responses after creating a contact message.
    Includes confirmation fields and read-only fields.
    """
    
    class Meta:
        model = ContactMessage
        fields = [
            'id',
            'name',
            'email',
            'message',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at']
