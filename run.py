import json
import sys

from Generator.Constructor import Constructor
from Serializer import DiagramSerializer

print()
diagram = DiagramSerializer(source="test(xml).xml")
diagram.dump()

with open(file='test(xml).json', mode='r') as f:
    data = json.loads(f.read())
constructor = Constructor(elements=data["root"])
f.close()
constructor.construct()
