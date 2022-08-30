about_us_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "minLength": 2, "maxLength": 80},
        "sub_title": {"type": "string", "maxLength": 120},
        "description": {"type": "string"}
      },
    "required": ["title"]
}
