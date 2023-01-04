#!/usr/bin/python3
""" create a unique storage instance to FileStorage """
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()


__all__ = ["BaseModel"]
