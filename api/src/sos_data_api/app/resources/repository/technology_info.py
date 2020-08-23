from ..entity.models import Technology
from ...models.repository.technology_base import TechnologyBase


class TechnologyInfo(TechnologyBase):

    def perssit(self, tech: Technology) -> None:
        pass

    def find_by_name(self, name: str) -> None:
        pass

    def find_by_uid(self, u_id: str) -> None:
        pass

    def update(self, tech: Technology) -> None:
        pass

    def add_tags(self, tech: Technology, new_tags: List[str]) -> None:
        pass

    def delete(self, tech: Technology) -> None:
        pass
