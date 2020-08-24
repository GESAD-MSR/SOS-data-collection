from ...models.entity.technology import Technology
from ..collections.technology_data import TechnologyData
from ...models.repository.technology_base import TechnologyBase


class TechnologyInfo(TechnologyBase):

    def perssit(self, tech: Technology) -> None:
        """docstring"""
        TechnologyData(name=tech.name, tags=tech.tags).save()

    def find_by_name(self, name: str) -> dict:
        """docstring"""
        return TechnologyData.objects(name=name).first()

    def find_by_uid(self, u_id: str) -> None:
        return TechnologyData.objects(_id=u_id).first()

    def update(self, tech: Technology) -> None:
        """TODO"""
        pass

    def add_tags_by_name(self, name: str, new_tags: List[str]) -> None:
        """docstring"""
        data = self.find_by_name(name)
        tech = Technology(
            u_id=data["_id"], name=data["name"], tags=data["tags"])

        tech.tags += new_tags
        # check if id does upsert!
        self.perssit(tech)

    def delete(self, tech: Technology) -> None:
        """TODO"""
        pass
