from rest_framework import generics, status
from rest_framework.response import Response
from contact.models import ContactMessage
from .serializers import ContactMessageCreateSerializer, ContactMessageResponseSerializer


class ContactMessageCreateView(generics.CreateAPIView):
    """
    API view for creating new contact messages.
    Accepts POST requests with contact form data and creates a new message.
    """
    serializer_class = ContactMessageCreateSerializer
    queryset = ContactMessage.objects.all()
    
    def create(self, request, *args, **kwargs):
        """
        Create a new contact message and return a success response.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        contact_message = serializer.save()
        
        # Use response serializer for the response
        response_serializer = ContactMessageResponseSerializer(contact_message)
        
        return Response(
            {
                'message': 'Contact message sent successfully!',
                'data': response_serializer.data
            },
            status=status.HTTP_201_CREATED
        )
