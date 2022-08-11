auth_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "minLength": 2, "maxLength": 60},
        "password": {"type": "string", "minLength": 6, "maxLength": 18},
      },
    "required": ["name"]
}
