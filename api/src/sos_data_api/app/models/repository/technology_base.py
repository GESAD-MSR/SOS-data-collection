from collections.abc import ABC, abstractmethod
from typing import NoReturn

from ..entity.technology import Technology


class TechnologyBase(ABC):

    @abstractmethod
    def create(self, tech: Technology) -> NoReturn:
        raise NotImplementedError()

    @abstractmethod
    def find_by_name(self, name: str) -> NoReturn:
        raise NotImplementedError()

    @abstractmethod
    def update(self, tech: Technology) -> NoReturn:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, tech: Technology) -> NoReturn:
        raise NotImplementedError()
