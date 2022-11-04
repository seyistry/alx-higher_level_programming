#!/usr/bin/python3
"""A Base class for this module"""

import json
import csv


class Base:
    """Base Class
       with private attr __nb_object
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ base constructor

        Args:
            id (int, None): can be a None or a +int
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert dict to json

        Args:
            list_dictionaries (dict): _description_

        Returns:
            dict: json dumps
        """
        if (list_dictionaries is None) or (len(list_dictionaries) == 0):
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file

        Args:
            list_objs (_type_): _description_
        """
        file = []
        file_name = cls.__name__ + ".json"
        if list_objs is not None:
            for i in list_objs:
                file.append(cls.to_dictionary(i))
        with open(file_name, "w") as fp:
            fp.write(cls.to_json_string(file))

    def from_json_string(json_string):
        """convert from jsonString to dict

        Args:
            json_string (_type_): _description_

        Returns:
            object: _description_
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load from file"""
        filename = cls.__name__ + ".json"
        file = []
        try:
            with open(filename, 'r') as fp:
                file = cls.from_json_string(fp.read())
            for i, e in enumerate(file):
                file[i] = cls.create(**file[i])
        except Exception:
            pass
        return file

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """using csv"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    csv_writer.writerow([obj.id, obj.width, obj.height,
                                         obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    csv_writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """load from csv"""
        filename = cls.__name__ + ".csv"
        row = []
        with open(filename, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for args in csv_reader:
                if cls.__name__ == "Rectangle":
                    dictionary = {"id": int(args[0]),
                                  "width": int(args[1]),
                                  "height": int(args[2]),
                                  "x": int(args[3]),
                                  "y": int(args[4])}
                elif cls.__name__ == "Square":
                    dictionary = {"id": int(args[0]), "size": int(args[1]),
                                  "x": int(args[2]), "y": int(args[3])}
                obj = cls.create(**dictionary)
                row.append(obj)
        return row
