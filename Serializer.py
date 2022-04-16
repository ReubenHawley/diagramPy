""""
A string parser for drawio xml files
"""
import re
import json
import xmltodict


class DiagramSerializer:
    """"
    Diagram is the master class that all child classes will inherit from
    """
    source: str
    elements: list
    element_pattern: str = r"<mxCell[^<>]+>"
    Attribute_pattern: str = r"(\w+)=(\"?)\w+\-\-w+(\"?)"

    def __init__(self, source: str):
        self.source = source

    def xml_parser(self) -> dict:
        # open the input xml file and read
        # data in form of python dictionary
        # using xmltodict module
        with open(self.source) as xml_file:
            data_dict = xmltodict.parse(xml_file.read())
            xml_file.close()
        return data_dict

    def find_elements(self) -> list:
        """
        Parse the xml document to find the mxCell elements which host the attributes for class assignment
        :return:
        """
        with open(self.source) as file:
            lines = file.read()
            # p = re.compile(r"(<mxCell).+")

            p = re.compile(r"<mxCell[^<>]+>")
            self.elements = p.findall(lines)
            return self.elements


if __name__ == '__main__':
    diagram = Diagram(source="test(xml).xml")
    elements = diagram.find_elements()
    print(elements)
