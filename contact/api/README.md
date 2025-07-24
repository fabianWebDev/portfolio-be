# Contact API

This directory contains the REST API endpoints for the contact application.

## Endpoints

### Create Contact Message
- **URL**: `/contact/api/contact/`
- **Method**: `POST`
- **Description**: Creates a new contact message from the contact form
- **Request Body**: JSON with contact form data
- **Response**: Success message with created message data

## Request Format

```json
{
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "+1234567890",  // Optional
    "subject": "General Inquiry",  // Optional
    "message": "Hello, I would like to discuss a project..."
}
```

## Response Format

```json
{
    "message": "Contact message sent successfully!",
    "data": {
        "id": 1,
        "name": "John Doe",
        "email": "john@example.com",
        "subject": "General Inquiry",
        "message": "Hello, I would like to discuss a project...",
        "created_at": "2024-01-15T10:30:00Z"
    }
}
```

## Serializers

### ContactMessageCreateSerializer
Used for creating new contact messages. Includes validation to ensure either phone or email is provided.

### ContactMessageResponseSerializer
Used for API responses, includes confirmation data and read-only fields.

## Features

- Custom validation ensuring either phone or email is provided
- Automatic timestamp creation
- Success response with created message data
- Proper HTTP status codes (201 for creation)
- Input validation and error handling

## Usage Examples

```bash
# Create a new contact message
curl -X POST http://localhost:8000/contact/api/contact/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "subject": "Project Discussion",
    "message": "I would like to discuss a potential project."
  }'
```

## Validation Rules

- `name`: Required, max 100 characters
- `email`: Required if phone not provided, must be valid email format
- `phone`: Optional, max 20 characters
- `subject`: Optional, max 200 characters
- `message`: Required, text content
- At least one of `email` or `phone` must be provided 