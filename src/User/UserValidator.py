user_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "minLength": 2, "maxLength": 60},
        "first_name": {"type": "string", "minLength": 2, "maxLength": 24},
        "last_name": {"type": "string", "minLength": 2, "maxLength": 24},
        "password": {"type": "string", "minLength": 6, "maxLength": 18},
      },
    "required": ["name", "first_name", "last_name", "password"]
}
