from abc import ABC, abstractmethod


class IGenerator(ABC):
    """"
    Abstract class to form the contract for the implementing classes
    """

    @abstractmethod
    def generate_document(self, path: str, generated_code: str):
        """"
        Create the documents
        """
        pass

    @abstractmethod
    def generate_class(self):
        """"
        Create new class
        """
        pass

    @abstractmethod
    def generate_attributes(self):
        """"
        Create new class
        """
        pass

    @abstractmethod
    def generate_methods(self):
        """"
        Create new class
        """
        pass
