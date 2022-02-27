import os
from abc import ABC, abstractmethod


class IGenerator(ABC):
    """"
    Abstract class to form the contract for the implementing classes
    """
    _diagram_type: str
    _primitive_string: str
    _primitive_int: str
    _primitive_double: str
    _primitive_float: str
    _primitive_array: str
    _primitive_object: str
    _primitive_void: str
    _private_prefix: str
    _protected_prefix: str
    _public_prefix: str

    @staticmethod
    def _generate_directory(path: str = None) -> None:
        try:
            os.mkdir(path)
        except FileNotFoundError():
            print("specified path does not exist")

    @abstractmethod
    def generate_document(self, path: str, generated_code: str):
        """"
        Create the documents
        """
        pass

    @abstractmethod
    def generate_class(self):
        """"
        Create new class
        """
        pass

    @abstractmethod
    def generate_attributes(self):
        """"
        Create new class
        """
        pass

    @abstractmethod
    def generate_methods(self):
        """"
        Create new class
        """
        pass

    @staticmethod
    def _capitalize_first(input_value: str) -> str:
        return_value = input_value[0].upper()
        return_value += input_value[1:].lower()
        return return_value

