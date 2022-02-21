""""
A string parser for drawio xml files
"""
import re


class Diagram:
    """"
    Diagram is the master class that all child classes will inherit from
    """
    source: str
    elements: list
    element_pattern: str = r"<mxCell[^<>]+>"
    Attribute_pattern: str = r"(\w+)=(\"?)\w+\-\-w+(\"?)"

    def __init__(self, source: str):
        self.source = source

    def find_elements(self)-> list:
        """
        Parse the xml document to find the mxCell elements which host the attributes for class assignment
        :return:
        """
        with open("test(xml).xml") as file:
            lines = file.read()
            # p = re.compile(r"(<mxCell).+")

            p = re.compile(r"<mxCell[^<>]+>")
            self.elements = p.findall(lines)
            return self.elements