import json
from copyreg import constructor

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
            generated_code = Java(self.elements)
        elif self.language == "csharp":
            generated_code = CSharp(self.elements)
        elif self.language == "python":
            for group in self.elements:
                constructor = Py("class", group)
                generated_code = constructor.generate_class()
                generated_code += constructor.generate_attributes()
                generated_code += constructor.generate_methods()
                constructor.generate_document(generated_code=generated_code, path="uglydiagrams/")
                print("success")


if __name__ == '__main__':
    elements = {"elements": ['<mxCell id="WIyWlLk6GJQsqaUBKTNV-0"/>',
                             '<mxCell id="WIyWlLk6GJQsqaUBKTNV-1" parent="WIyWlLk6GJQsqaUBKTNV-0"/>',
                             '<mxCell id="zkfFHV4jXpPFQw0GAbJ--0" value="Person" '
                             'style="swimlane;fontStyle=2;align=center;verticalAlign=top;childLayout=stackLayout'
                             ';horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeLast=0;collapsible=1'
                             ';marginBottom=0;rounded=0;shadow=0;strokeWidth=1;" parent="WIyWlLk6GJQsqaUBKTNV-1" '
                             'vertex="1">',
                             '<mxCell id="zkfFHV4jXpPFQw0GAbJ--1" value="- Name: String"\n                        '
                             'style="text;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden'
                             ';rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;"\n                       '
                             ' parent="zkfFHV4jXpPFQw0GAbJ--0" vertex="1">',
                             '<mxCell id="zkfFHV4jXpPFQw0GAbJ--2" value="- PhoneNumber: int"\n                        '
                             'style="text;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden'
                             ';rotatable=0;points=[[0,0.5],[1,'
                             '0.5]];portConstraint=eastwest;rounded=0;shadow=0;html=0;"\n                        '
                             'parent="zkfFHV4jXpPFQw0GAbJ--0" vertex="1">',
                             '<mxCell id="zkfFHV4jXpPFQw0GAbJ--3" value="- EmailAddress: String"\n                    '
                             '    style="text;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow'
                             '=hidden;rotatable=0;points=[[0,0.5],[1,'
                             '0.5]];portConstraint=eastwest;rounded=0;shadow=0;html=0;"\n                        '
                             'parent="zkfFHV4jXpPFQw0GAbJ--0" vertex="1">',
                             '<mxCell id="zkfFHV4jXpPFQw0GAbJ--4" value=""\n                        '
                             'style="line;html=1;strokeWidth=1;align=left;verticalAlign=middle;spacingTop=-1'
                             ';spacingLeft=3;spacingRight=3;rotatable=0;labelPosition=right;points=['
                             '];portConstraint=eastwest;"\n                        parent="zkfFHV4jXpPFQw0GAbJ--0" '
                             'vertex="1">',
                             '<mxCell id="zkfFHV4jXpPFQw0GAbJ--5" value="+ GetName(): String"\n                       '
                             ' style="text;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden'
                             ';rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;"\n                       '
                             ' parent="zkfFHV4jXpPFQw0GAbJ--0" vertex="1">',
                             '<mxCell id="zkfFHV4jXpPFQw0GAbJ--6" value="Student"\n                        '
                             'style="swimlane;fontStyle=0;align=center;verticalAlign=top;childLayout=stackLayout'
                             ';horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeLast=0;collapsible=1'
                             ';marginBottom=0;rounded=0;shadow=0;strokeWidth=1;"\n                        '
                             'parent="WIyWlLk6GJQsqaUBKTNV-1" vertex="1">',
                             '<mxCell id="zkfFHV4jXpPFQw0GAbJ--7" value="Student Number"\n                        '
                             'style="text;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden'
                             ';rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;"\n                       '
                             ' parent="zkfFHV4jXpPFQw0GAbJ--6" vertex="1">',
                             '<mxCell id="zkfFHV4jXpPFQw0GAbJ--8" value="Average Mark"\n                        '
                             'style="text;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden'
                             ';rotatable=0;points=[[0,0.5],[1,'
                             '0.5]];portConstraint=eastwest;rounded=0;shadow=0;html=0;"\n                        '
                             'parent="zkfFHV4jXpPFQw0GAbJ--6" vertex="1">',
                             '<mxCell id="zkfFHV4jXpPFQw0GAbJ--9" value=""\n                        '
                             'style="line;html=1;strokeWidth=1;align=left;verticalAlign=middle;spacingTop=-1'
                             ';spacingLeft=3;spacingRight=3;rotatable=0;labelPosition=right;points=['
                             '];portConstraint=eastwest;"\n                        parent="zkfFHV4jXpPFQw0GAbJ--6" '
                             'vertex="1">',
                             '<mxCell id="zkfFHV4jXpPFQw0GAbJ--10" value="Is Eligible To Enroll"\n                    '
                             '    style="text;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow'
                             '=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;fontStyle=4"\n     '
                             '                   parent="zkfFHV4jXpPFQw0GAbJ--6" vertex="1">',
                             '<mxCell id="zkfFHV4jXpPFQw0GAbJ--11" value="Get Seminars Taken"\n                       '
                             ' style="text;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden'
                             ';rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;"\n                       '
                             ' parent="zkfFHV4jXpPFQw0GAbJ--6" vertex="1">',
                             '<mxCell id="zkfFHV4jXpPFQw0GAbJ--12" value=""\n                        '
                             'style="endArrow=block;endSize=10;endFill=0;shadow=0;strokeWidth=1;rounded=0;edgeStyle'
                             '=elbowEdgeStyle;elbow=vertical;"\n                        '
                             'parent="WIyWlLk6GJQsqaUBKTNV-1" source="zkfFHV4jXpPFQw0GAbJ--6" '
                             'target="zkfFHV4jXpPFQw0GAbJ--0"\n                        edge="1">',
                             '<mxCell id="zkfFHV4jXpPFQw0GAbJ--13" value="Professor"\n                        style="swimlane;fontStyle=0;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeLast=0;collapsible=1;marginBottom=0;rounded=0;shadow=0;strokeWidth=1;"\n                        parent="WIyWlLk6GJQsqaUBKTNV-1" vertex="1">',
                             '<mxCell id="zkfFHV4jXpPFQw0GAbJ--14" value="Salary"\n                        '
                             'style="text;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden'
                             ';rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;"\n                       '
                             ' parent="zkfFHV4jXpPFQw0GAbJ--13" vertex="1">',
                             '<mxCell id="zkfFHV4jXpPFQw0GAbJ--15" value=""\n                        style="line;html=1;strokeWidth=1;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=3;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;"\n                        parent="zkfFHV4jXpPFQw0GAbJ--13" vertex="1">',
                             '<mxCell id="zkfFHV4jXpPFQw0GAbJ--16" value=""\n                        style="endArrow=block;endSize=10;endFill=0;shadow=0;strokeWidth=1;rounded=0;edgeStyle=elbowEdgeStyle;elbow=vertical;"\n                        parent="WIyWlLk6GJQsqaUBKTNV-1" source="zkfFHV4jXpPFQw0GAbJ--13" target="zkfFHV4jXpPFQw0GAbJ--0"\n                        edge="1">',
                             '<mxCell id="zkfFHV4jXpPFQw0GAbJ--17" value="Address"\n                        style="swimlane;fontStyle=0;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeLast=0;collapsible=1;marginBottom=0;rounded=0;shadow=0;strokeWidth=1;"\n                        parent="WIyWlLk6GJQsqaUBKTNV-1" vertex="1">',
                             '<mxCell id="zkfFHV4jXpPFQw0GAbJ--18" value="Street: String"\n                        style="text;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;"\n                        parent="zkfFHV4jXpPFQw0GAbJ--17" vertex="1">',
                             '<mxCell id="zkfFHV4jXpPFQw0GAbJ--19" value="City"\n                        style="text;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;rounded=0;shadow=0;html=0;"\n                        parent="zkfFHV4jXpPFQw0GAbJ--17" vertex="1">',
                             '<mxCell id="zkfFHV4jXpPFQw0GAbJ--20" value="State"\n                        style="text;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;rounded=0;shadow=0;html=0;"\n                        parent="zkfFHV4jXpPFQw0GAbJ--17" vertex="1">',
                             '<mxCell id="zkfFHV4jXpPFQw0GAbJ--21" value="Postal Code"\n                        style="text;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;rounded=0;shadow=0;html=0;"\n                        parent="zkfFHV4jXpPFQw0GAbJ--17" vertex="1">',
                             '<mxCell id="zkfFHV4jXpPFQw0GAbJ--22" value="Country"\n                        style="text;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;rounded=0;shadow=0;html=0;"\n                        parent="zkfFHV4jXpPFQw0GAbJ--17" vertex="1">',
                             '<mxCell id="zkfFHV4jXpPFQw0GAbJ--23" value=""\n                        style="line;html=1;strokeWidth=1;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=3;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;"\n                        parent="zkfFHV4jXpPFQw0GAbJ--17" vertex="1">',
                             '<mxCell id="zkfFHV4jXpPFQw0GAbJ--24" value="Validate"\n                        style="text;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;"\n                        parent="zkfFHV4jXpPFQw0GAbJ--17" vertex="1">',
                             '<mxCell id="zkfFHV4jXpPFQw0GAbJ--25" value="Output As Label"\n                        style="text;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;"\n                        parent="zkfFHV4jXpPFQw0GAbJ--17" vertex="1">',
                             '<mxCell id="zkfFHV4jXpPFQw0GAbJ--26" value=""\n                        style="endArrow=open;shadow=0;strokeWidth=1;rounded=0;endFill=1;edgeStyle=elbowEdgeStyle;elbow=vertical;"\n                        parent="WIyWlLk6GJQsqaUBKTNV-1" source="zkfFHV4jXpPFQw0GAbJ--0" target="zkfFHV4jXpPFQw0GAbJ--17"\n                        edge="1">',
                             '<mxCell id="zkfFHV4jXpPFQw0GAbJ--27" value="0..1"\n                        style="resizable=0;align=left;verticalAlign=bottom;labelBackgroundColor=none;fontSize=12;"\n                        parent="zkfFHV4jXpPFQw0GAbJ--26" connectable="0" vertex="1">',
                             '<mxCell id="zkfFHV4jXpPFQw0GAbJ--28" value="1"\n                        style="resizable=0;align=right;verticalAlign=bottom;labelBackgroundColor=none;fontSize=12;"\n                        parent="zkfFHV4jXpPFQw0GAbJ--26" connectable="0" vertex="1">',
                             '<mxCell id="zkfFHV4jXpPFQw0GAbJ--29" value="lives at"\n                        style="text;html=1;resizable=0;points=[];;align=center;verticalAlign=middle;labelBackgroundColor=none;rounded=0;shadow=0;strokeWidth=1;fontSize=12;"\n                        parent="zkfFHV4jXpPFQw0GAbJ--26" vertex="1" connectable="0">',
                             '<mxCell id="k8z_hRTHZBopF7ecELwy-16"\n                        value="&lt;p style=&quot;margin: 0px ; margin-top: 4px ; text-align: center&quot;&gt;&lt;b&gt;RandomClass&lt;/b&gt;&lt;/p&gt;&lt;hr size=&quot;1&quot;&gt;&lt;p style=&quot;margin: 0px ; margin-left: 4px&quot;&gt;+ publicField: String&lt;/p&gt;&lt;hr size=&quot;1&quot;&gt;&lt;p style=&quot;margin: 0px ; margin-left: 4px&quot;&gt;+ method(): Type&lt;/p&gt;"\n                        style="verticalAlign=top;align=left;overflow=fill;fontSize=12;fontFamily=Helvetica;html=1;"\n                        vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">']}
    with open(file='../mockup.json', mode='r') as f:
        data = json.loads(f.read())
    constructor = Constructor(elements=data["root"])
    f.close()
    constructor.construct()
