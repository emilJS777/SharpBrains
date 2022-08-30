auth_schema = {
    "type": "object",
    "properties": {
        "email_address": {"type": "string", "minLength": 2, "maxLength": 60},
        "password": {"type": "string", "minLength": 6, "maxLength": 18},
      },
    "required": ["email_address"]
}
