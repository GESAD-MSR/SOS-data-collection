from typing import List


class Technology(object):
    """docstring"""

    def __init__(self, u_id: str name: str, tags: List[str]):
        self.__u_id = u_id
        self.__name = name
        self.__tags = tags

    @property
    def u_id(self) -> str:
        return self.__u_id

    @u_id.setter
    def u_id(self, new_u_id: str) -> None:
        self.__u_id = new_u_id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        self.__name = new_name

    @property
    def tags(self) -> List[str]:
        return self.__tags

    @tags.setter
    def tags(self, new_tags) -> None:
        self.__tags = new_tags
