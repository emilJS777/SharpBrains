role_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "minLength": 1, "maxLength": 120},
        "description": {"type": "string", "maxLength": 120},
        "permission_ids": {"type": "array"},
      },
    "required": ["name", "permission_ids"]
}