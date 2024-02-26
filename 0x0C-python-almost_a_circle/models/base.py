#!/usr/bin/python3
import json

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON-formatted string"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of objects to a JSON file"""
        # Convert list of objects to list of dictionaries
        list_dicts = [obj.to_dictionary() for obj in list_objs] if list_objs is not None else []

        # Get class name for filename
        class_name = cls.__name__
        filename = f"{class_name}.json"

        # Write JSON string to file
        with open(filename, 'w') as file:
            file.write(cls.to_json_string(list_dicts))

