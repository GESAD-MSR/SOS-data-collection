from collections.abc import ABC, abstractmethod
from typing import NoReturn, List

from ..entity.technology import Technology


class TechnologyBase(ABC):

    @abstractmethod
    def perssit(self, tech: Technology) -> NoReturn:
        raise NotImplementedError()

    @abstractmethod
    def find_by_name(self, name: str) -> NoReturn:
        raise NotImplementedError()

    @abstractmethod
    def find_by_uid(self, u_id: str) -> NoReturn:
        raise NotImplementedError()

    @abstractmethod
    def update(self, tech: Technology) -> NoReturn:
        raise NotImplementedError()

    @abstractmethod
    def add_tags(self, tech: Technology, new_tags: List[str]) -> NoReturn:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, tech: Technology) -> NoReturn:
        raise NotImplementedError()
