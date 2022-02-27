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
    _primitive_boolean: str
    _empty_string: str = '\"\"'
    _empty_int: int = 0
    _empty_float: float = 0
    _empty_double: float = 0
    _private_prefix: str
    _protected_prefix: str
    _public_prefix: str
    _extension: str

    def __init__(self, diagram_type: str, elements: dict) -> None:
        self.elements = elements
        self._diagram_type = diagram_type
        self.class_name = self._capitalize_first(self.elements['class'])

    @staticmethod
    def _generate_directory(path: str = None) -> None:
        try:
            os.mkdir(path)
        except FileNotFoundError():
            print("specified path does not exist")

    def generate_document(self, generated_code: str, path: str = None) -> None:
        """"
        Create the documents
        """
        if path is None:
            path = os.path.join(os.getcwd(), f"{self._diagram_type}_diagram")
        if os.path.exists(path):
            with open(f'{path}/{self.class_name}{self._extension}', 'w') as file:
                file.write(generated_code)
        else:
            self._generate_directory(path)
            with open(f'{path}/{self.class_name}{self._extension}', 'w') as file:
                file.write(generated_code)

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

    def _parse_datatype(self, input_type: str) -> str:
        if input_type.__eq__("string"):
            return self._primitive_string
        elif input_type.__eq__("int"):
            return self._primitive_int
        elif input_type.__eq__("double"):
            return self._primitive_double
        elif input_type.__eq__("float"):
            return self._primitive_float
        elif input_type.__eq__("void"):
            return self._primitive_void
        if input_type.__eq__("boolean"):
            return self._primitive_boolean

    def _parse_returntype(self, returntype: str):
        if returntype.__eq__("int"):
            return self._empty_int
        elif returntype.__eq__("float"):
            return self._empty_float
        elif returntype.__eq__("boolean"):
            return self._empty_boolean
        elif returntype.__eq__("string"):
            return self._empty_string
        elif returntype.__eq__("double"):
            return self._empty_double

