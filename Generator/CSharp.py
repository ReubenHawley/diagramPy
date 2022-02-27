from Generator.IGenerator import IGenerator


class CSharp(IGenerator):
    """"
    Generator for the c# code, parent of IGenerator and child of Constructor Class
    """

    elements: dict

    def __init__(self, elements: dict) -> None:
        self.elements = elements

    def generate_document(self):
        """"
        Create the documents
        """
        pass

    def generate_class(self):
        """"
        Create new class
        """
        pass

    def generate_attributes(self):
        """"
        Create new class
        """
        pass

    def generate_methods(self):
        """"
        Create new class
        """
        pass
