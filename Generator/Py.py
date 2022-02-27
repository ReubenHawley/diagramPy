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
    _primitive_void: str = "None"
    _private_prefix: str = "_"
    _protected_prefix: str = "__"
    _public_prefix: str = ""

    def __init__(self, diagram_type: str, elements: dict) -> None:
        self.elements = elements
        self._diagram_type = diagram_type
        self.class_name = self.__capitalize_first(self.elements['class'])

    def generate_document(self, generated_code: str, path: str = None) -> None:
        """"
        Create the documents
        """
        if path is None:
            path = os.path.join(os.getcwd(), f"{self._diagram_type}_diagram")
        if os.path.exists(path):
            with open(f'{path}/{self.class_name}.py', 'w') as file:
                file.write(generated_code)
        else:
            os.mkdir(path)
            with open(f'{path}/{self.class_name}.py', 'w') as file:
                file.write(generated_code)

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
            parsed_datatype = self.__parse_datatype(atter['datatype'])
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
                    parameter_type = self.__parse_datatype(parameter["datatype"])
                    string_methods += f", {parameter['name'].lower()}: {parameter_type}"
            return_datatype = self.__parse_datatype(method['datatype'])
            string_methods += f") -> {return_datatype}:\n\t\tpass\n\n"

        return string_methods

    @staticmethod
    def __capitalize_first(input_value: str) -> str:
        return_value = input_value[0].upper()
        return_value += input_value[1:].lower()
        return return_value

    def __parse_datatype(self, input_type: str) -> str:
        if input_type == "String":
            return self._primitive_string
        if input_type == "Integer":
            return self._primitive_int
        if input_type == "Double":
            return self._primitive_double
        if input_type == "Float":
            return self._primitive_float
        if "[]" in input_type:
            return self._primitive_array
        # if input_type == :
        #     return self.primitive_object
