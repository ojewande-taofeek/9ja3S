#!/usr/bin/python3
"""
    Creates an instance of the storage
"""
from seniors.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
