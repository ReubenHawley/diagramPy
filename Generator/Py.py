import os.path

from Generator.IGenerator import IGenerator


class Py(IGenerator):
    """"
    Generator for the python code, parent of IGenerator and child of Constructor Class
    """
    elements: dict
    _diagram_type: str
    _primitive_string: str = "str"
    _primitive_int: str = "int"
    _primitive_double: str = "float"
    _primitive_float: str = "float"
    _primitive_array: str = "list"
    _primitive_object: str = "object"
    _primitive_boolean: str = "bool"
    _primitive_void: str = "None"
    _private_prefix: str = "_"
    _protected_prefix: str = "__"
    _public_prefix: str = ""
    _extension = ".py"

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
            self._generate_module(path)
            with open(f'{path}/{self.class_name}{self._extension}', 'w') as file:
                file.write(generated_code)

    @staticmethod
    def _generate_module(path):
        try:
            with open(f'{path}/__init__.py', 'w') as file:
                file.write("")
        except FileNotFoundError():
            print("specified path does not exist")

    def generate_class(self) -> str:
        """"
        Create new class using the dictionary assigned to elements
        """
        string_class = f"class {self.class_name}:\n"
        return string_class

    def generate_attributes(self):
        """"
        Create new attributes
        """
        string_atters = ""
        for atter in self.elements["attributes"]:
            parsed_datatype = self._parse_datatype(atter['datatype'])
            string_atters += f"\t"
            if atter["Access"] == "private":
                string_atters += self._private_prefix
            elif atter["Access"] == "protected":
                string_atters += self._protected_prefix
            elif atter["Access"] == "public":
                string_atters += self._public_prefix
            else:
                raise ValueError(f"unexpected value received: {atter['Access']}")
            string_atters += f"{atter['AttributeName']}: {parsed_datatype}\n"

        string_atters += "\n"
        return string_atters

    def generate_methods(self):
        """"
        Create new class methods
        """
        string_methods = f"\tdef __init__(self) -> None:\n\t\tpass\n\n"
        for method in self.elements["methods"]:
            string_methods += f"\tdef "
            if method["Access"] == "private":
                string_methods += self._private_prefix
            elif method["Access"] == "protected":
                string_methods += self._protected_prefix
            elif method["Access"] == "public":
                string_methods += self._public_prefix
            else:
                raise ValueError(f"unexpected value received: {method['Access']}")
            string_methods += f"{method['methodName'].lower()}(self"

            if "Parameters" in method:
                for parameter in method["Parameters"]:
                    parameter_type = self._parse_datatype(parameter["datatype"])
                    string_methods += f", {parameter['name'].lower()}: {parameter_type}"
            return_datatype = self._parse_datatype(method['datatype'])
            string_methods += f") -> {return_datatype}:\n\t\tpass\n\n"

        return string_methods
