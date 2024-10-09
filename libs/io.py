import abc
from typing import Any


class Writer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def write(self, data: Any):
        pass
