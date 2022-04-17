
from Generator.CSharp import CSharp
from Generator.Java import Java
from Generator.Py import Py


class Constructor:
    """
    Constructor takes a dictionary object and converts it and then calls the concrete constructor classes

    """
    elements: dict
    language: str
    valid_languages = ["csharp", "java", "python"]

    def __init__(self, elements: dict) -> None:
        self.elements = elements
        try:
            self.define_language()
        except ValueError:
            print("invalid input given, values should be 'csharp','java' or 'python'")
            self.define_language()

    def define_language(self) -> None:
        """
        Take user input if args not passed with cmd
        """
        self.language = input("Enter the output language:\n")
        if self.language not in self.valid_languages:
            raise ValueError("invalid input given, values should be 'csharp','java' or 'python'")

    def construct(self) -> None:
        """
            Uses the defined language to call the relevant constructor class
        """

        if self.language == "java":
            for group in self.elements:
                constructor = Java("class", group)
                generated_code = constructor.generate_class()
                generated_code += constructor.generate_attributes()
                generated_code += constructor.generate_methods()
                generated_code += constructor.close_class()
                constructor.generate_document(generated_code=generated_code)

                print("success")
        elif self.language == "csharp":
            constructor = CSharp(self.elements)
        elif self.language == "python":
            for group in self.elements:
                constructor = Py("class", group)
                generated_code = constructor.generate_class()
                generated_code += constructor.generate_attributes()
                generated_code += constructor.generate_methods()
                constructor.generate_document(generated_code=generated_code)
                print("success")

