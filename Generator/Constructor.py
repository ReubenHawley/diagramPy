class Constructor:
    """
    Constructor takes a dictionary object and converts it and then calls the concrete constructor classes

    """
    elements: dict
    language: str
    valid_languages = ["csharp","java","python"]

    def __init__(self, elements: dict) -> None:
        self.elements = elements

    def define_language(self) -> None:
        """
        Take user input if args not passed with cmd
        """
        self.language = input("Enter the output language")
        if self.language not in self.valid_languages:
            raise ValueError("invalid input given, values should be \"csharp\",\"java\" or \"python\"")
