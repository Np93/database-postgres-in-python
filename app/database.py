from tortoise.contrib.fastapi import register_tortoise, HTTPNotFoundError
import os

DATABASE_URL = os.getenv("DATABASE_URL")

def init_db(app):
    register_tortoise(
        app,
        config={
            "connections": {"default": DATABASE_URL},
            "apps": {
                "models": {
                    "models": ["app.models", "aerich.models"],
                    "default_connection": "default",
                },
            },
        },
        generate_schemas=True,
        add_exception_handlers=True,
    )