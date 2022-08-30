user_schema = {
    "type": "object",
    "properties": {
        "email_address": {"type": "string", "minLength": 2, "maxLength": 60},
        "first_name": {"type": "string", "minLength": 2, "maxLength": 24},
        "last_name": {"type": "string", "minLength": 2, "maxLength": 24},
      },
    "required": ["email_address", "first_name", "last_name"]
}

user_registration_schema = {
    "type": "object",
    "properties": {
        "ticket": {"type": "string", "minLength": 1, "maxLength": 120},
        "password": {"type": "string", "minLength": 6, "maxLength": 18},
      },
    "required": ["ticket", "password"]
}
