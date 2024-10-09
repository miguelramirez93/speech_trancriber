import abc
from typing import Any


class Writer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def write(self, data: Any):
        pass


class FileWriter(Writer):
    def __init__(self, filepath: str) -> None:
        self.__file_path = filepath

    def write(self, data: Any):
        with open(self.__file_path, "a") as f:
            f.write(f"{data} \n")
