# Projects API

This directory contains the REST API endpoints for the projects application.

## Endpoints

### List Projects
- **URL**: `/projects/api/`
- **Method**: `GET`
- **Description**: Returns a list of all active projects with essential information
- **Response**: List of projects with fields: `id`, `name`, `image`, `short_description`, `tech_list`, `link`, `github_url`, `is_active`, `created_at`

### Project Detail
- **URL**: `/projects/api/{id}/`
- **Method**: `GET`
- **Description**: Returns detailed information about a specific project
- **Response**: Complete project object with all fields including full description and metadata

## Serializers

### ProjectListSerializer
Used for the list view, includes only essential fields for efficient listing.

### ProjectSerializer
Used for the detail view, includes all project fields and computed properties like `tech_list` and `display_name`.

## Features

- Only active projects are returned (`is_active=True`)
- Projects are ordered by creation date (newest first)
- Automatic 404 responses for inactive or non-existent projects
- Computed fields like `tech_list` (technologies as a list) and `display_name`
- Full validation and error handling

## Usage Examples

```bash
# Get all projects
curl http://localhost:8000/projects/api/

# Get specific project
curl http://localhost:8000/projects/api/1/
``` 