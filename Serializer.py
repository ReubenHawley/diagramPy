""""
A string parser for drawio xml files
"""
import re
import json
from pprint import pprint

import xmltodict


class DiagramSerializer:
    """"
    Diagram is the master class that all child classes will inherit from
    """
    source: str
    elements: list
    element_pattern: str = r"<mxCell[^<>]+>"
    Attribute_pattern: str = r"(\w+)=(\"?)\w+\-\-w+(\"?)"
    json_file: dict = {"root": []}

    def __init__(self, source: str):
        self.source = source
        self.xml_elements: str = ""
        self.xml_parser()
        self.get_root()

    def xml_parser(self) -> dict:
        # open the input xml file and read
        # data in form of python dictionary
        # using xmltodict module
        with open(self.source) as xml_file:
            self.xml_elements = xmltodict.parse(xml_file.read())
            xml_file.close()
        return self.xml_elements

    def get_root(self) -> str:
        self.xml_elements = self.xml_elements['mxfile']["diagram"]["mxGraphModel"]["root"]["mxCell"]
        for diagramclass in self.xml_elements:
            # finds the page base and reassigns the element group
            if not diagramclass.__contains__("@parent"):
                self.xml_elements = self.xml_elements[1:]
        # assigns the first element of the element group as the root base
        self.json_file["Id"] = self.xml_elements[0]["@id"]
        return self.json_file["Id"]

    def get_classes(self) -> dict:
        """
        Parse the xml document to find the mxCell elements which host the attributes for class assignment
        :return:
        """
        class_list = []
        for diagramclass in self.xml_elements:
            # safeguard to only capture elements that have a parent attribute
            if diagramclass.__contains__("@parent"):
                # finds the class names in the diagram based on the root "Id"
                if diagramclass["@parent"] == self.json_file["Id"]:
                    # drops lines from the root diagram that have value of ""
                    if diagramclass["@value"] != "":
                        if "<" not in diagramclass["@value"]:
                            class_dictionary = {"Id": diagramclass["@id"],
                                                "class": diagramclass["@value"],
                                                "attributes": [],
                                                "methods": []}
                            class_list.append(class_dictionary)

        self.json_file["root"] = class_list
        return self.json_file

    def get_props(self) -> dict:
        for diagramclass in self.xml_elements:
            for class_name in self.json_file["root"]:
                if class_name["Id"] == diagramclass["@parent"]:
                    if diagramclass["@value"] != "":
                        if "()" in diagramclass["@value"]:
                            print(class_name["Id"])
                            print(diagramclass["@parent"])
                            pprint(diagramclass["@value"])
                # pprint(self.xml_elements)
        return self.json_file

    @staticmethod
    def map_methods(value_to_map) -> dict:
        access = ""
        MethodName = ""
        Datatype = ""
        Static = None

        # map the method Name
        MethodName = value_to_map

        # map the datatype
        Datatype = value_to_map

        # map the access modifiers
        if value_to_map[0] == ["-"]:
            access = "private"
        elif value_to_map[0] == ["+"]:
            access = "public"
        elif value_to_map[0] == ["~"]:
            access = "protected"

        # map the methodtype
        Static = False
        class_methods = {"methodName": "getName",
                         "datatype": "void",
                         "Access": access,
                         "static": Static}
        return class_methods


if __name__ == '__main__':
    diagram = DiagramSerializer(source="test(xml).xml")
    # print(diagram.json_file)
    diagram.get_classes()
    diagram.get_props()
    # pprint(diagram.json_file)
