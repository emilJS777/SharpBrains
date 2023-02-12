project_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "minLength": 2, "maxLength": 60},
        "description": {"type": "string", "maxLength": 120},
        "sphere_id": {"type": "number"},
        # "image_id": {"type": "number"},
        "project_status_id": {"type": "number"},
        "progress": {"type": "number", "minimum": 0, "maximum": 100},

        "owner_name": {"type": "string", "maxLength": 120},
        "email_address": {"type": "string", "maxLength": 120},
        "assigned_from": {"type": "string", "maxLength": 120},
      },
    "required": ["title"]
}
