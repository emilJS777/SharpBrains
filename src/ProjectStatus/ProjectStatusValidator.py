project_status_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "minLength": 2, "maxLength": 60},
        "description": {"type": "string", "maxLength": 120},
        "color": {"type": "string", "minLength": 2, "maxLength": 10}
      },
    "required": ["title"]
}
