from Generator.IGenerator import IGenerator


class Py(IGenerator):
    """"
    Generator for the python code, parent of IGenerator and child of Constructor Class
    """
    elements: dict
    diagram_type: str

    def __init__(self, diagram_type: str, elements: dict) -> None:
        self.elements = elements
        self.diagram_type = diagram_type

    def generate_document(self):
        """"
        Create the documents
        """
        open(f'generatedDoc/{self.diagram_type}', 'w')

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
