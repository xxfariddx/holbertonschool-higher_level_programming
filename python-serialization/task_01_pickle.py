#!/usr/bin/pyhton3
"""d w d"""
import pickle


class CustomObject:
    def __init__(self, name: str, age: int, is_student: bool):
        """sdfew"""
        self.name = name
        self.age = age
        self.is_student = is_student
    
    def display(self):
        """dffsd erwe"""
        print("Name: ".format(self.name))
        print("Age: ".format(self.age))
        print("Is_student: ".format(self.is_student))
    
    def serialize(self, filename):
        """sdfsd sdfdf"""
        try:
            with open(filename, mode="wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError):
            return None
    
    @classmethod
    def deserialize(cls, filename):
        """asd ff"""
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
            return None
        except (FileNotFoundError, EOFError, pickle.UnpicklingError, OSError):
            return None
