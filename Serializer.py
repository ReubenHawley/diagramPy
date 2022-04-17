""""
A string parser for drawio xml files
"""
import json
import os
from pprint import pprint

import xmltodict


class DiagramSerializer:
    """"
    Diagram is the master class that all child classes will inherit from
    """
    source: str
    elements: list
    json_file: dict = {"root": []}

    def __init__(self, source: str):
        self.source = source
        self.cwd = os.getcwd()
        self.xml_elements: str = ""
        self.xml_parser()
        self.get_root()
        self.get_classes()
        self.get_props()

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

    def get_props(self):
        counter = 0
        for class_name in self.json_file["root"]:
            methods = []
            attributes = []
            for diagramclass in self.xml_elements:
                try:
                    if class_name["Id"] == diagramclass["@parent"]:
                        if diagramclass["@value"] != "":
                            if "()" in diagramclass["@value"]:
                                methods.append(self.map_methods(diagramclass["@value"]))
                            else:
                                attributes.append(self.map_attributes(diagramclass["@value"]))
                except Exception:
                    print(" Failed to map methods and attributes, please check syntax")
            # mapping directly causes a nested list, using the list comprehension we escape this
            [self.json_file["root"][counter]["attributes"].append(atter) for atter in attributes]
            [self.json_file["root"][counter]["methods"].append(method_defintion) for method_defintion in methods]
            counter += 1

    def map_methods(self, value_to_map: str) -> dict:

        access, methodName, datatype = self.split(value_to_map)
        Static = "false"

        # parse methodName for user errors
        methodName = methodName.strip("():")

        # map the access modifiers
        access = self.map_access(access)

        datatype = datatype.lower()
        # create dictionary of method attributes
        class_methods = {"methodName": methodName,
                         "datatype": datatype,
                         "Access": access,
                         "static": Static}
        return class_methods

    def map_attributes(self, value_to_map: str) -> dict:

        access, attributeName, datatype = self.split(value_to_map)

        datatype = datatype.lower()
        # map access
        access = self.map_access(access)

        if ":" in attributeName:
            attributeName = attributeName.strip(":")

        # create dictionary of method attributes
        class_methods = {"AttributeName": attributeName,
                         "datatype": datatype,
                         "Access": access}
        return class_methods

    @staticmethod
    def map_access(access_modifier: str) -> str:
        access = ""
        if "-" in access_modifier:
            access = "private"
        elif "+" in access_modifier:
            access = "public"
        elif "~" in access_modifier:
            access = "protected"
        return access

    @staticmethod
    def split(value: str) -> list:
        return_value = value.split(" ")
        return return_value

    def dump(self, path=None):
        if path is None:
            path = self.cwd
        # Serializing json
        json_object = json.dumps(self.json_file, indent=4)

        source = self.source.strip(".xml")
        # Writing to sample.json
        with open(f"{path}\{source}.json", "w") as outfile:
            outfile.write(json_object)
