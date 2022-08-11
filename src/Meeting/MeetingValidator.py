meeting_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "minLength": 2, "maxLength": 60},
        "description": {"type": "string", "maxLength": 120},
        "date": {"type": "string"}
      },
    "required": ["title"]
}
