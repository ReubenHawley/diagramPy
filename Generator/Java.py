import os

from Generator.IGenerator import IGenerator


class Java(IGenerator):
    """"
    Generator for the Java code, parent of IGenerator and child of Constructor Class
    """
    elements: dict
    _primitive_string: str = "String"
    _primitive_int: str = "int"
    _primitive_double: str = "double"
    _primitive_float: str = "float"
    _primitive_array: str = "[]"
    _primitive_void: str = "void"
    _primitive_boolean: str = "boolean"
    _empty_boolean: bool = "false"
    _private_prefix: str = "private"
    _protected_prefix: str = "protected"
    _public_prefix: str = "public"
    _extension: str = ".java"

    def generate_class(self) -> str:
        """"
        Create new class using the dictionary assigned to elements
        """
        string_class = f"public class {self.class_name}"
        string_class += "{\n"
        return string_class

    @staticmethod
    def close_class() -> str:
        return "}"

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
            string_atters += f"  {parsed_datatype} {atter['AttributeName']};\n"

        string_atters += "\n"
        return string_atters

    def generate_methods(self):
        """"
        Create new class methods
        """
        string_methods = ""
        for method in self.elements["methods"]:
            string_methods += f"\t"
            if method["Access"] == "private":
                string_methods += self._private_prefix
            elif method["Access"] == "protected":
                string_methods += self._protected_prefix
            elif method["Access"] == "public":
                string_methods += self._public_prefix
            else:
                raise ValueError(f"unexpected value received: {method['Access']}")
            if method["datatype"].__eq__("string"):
                datatype = "String"
            else:
                datatype = method["datatype"]
            if method["static"] == "true":
                string_methods += f"static {method['datatype']} {self._capitalize_first(method['methodName'])}("
            elif method["static"] == "false":
                string_methods += f" {datatype} {self._capitalize_first(method['methodName'])}("

            if "Parameters" in method:
                for parameter in method["Parameters"]:
                    parameter_type = self._parse_datatype(parameter["datatype"])
                    if parameter["datatype"].__eq__("string"):
                        string_methods += f"{self._capitalize_first(parameter_type)} {parameter['name'].lower()}, "
                    else:
                        string_methods += f"{parameter_type} {parameter['name'].lower()}, "
                string_methods = string_methods[:-2]
            string_methods += "){\n\t"
            if not method["datatype"].__eq__("void"):
                string_methods += f"{datatype} x = {self._parse_returntype(method['datatype'])};\n"
                string_methods += "\treturn x;\n"
            string_methods += "}\n\n"

        return string_methods


