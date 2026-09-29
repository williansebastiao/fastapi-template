from math import ceil

from pydantic import BaseModel, ConfigDict, computed_field


class PageResponse[T](BaseModel):
    items: list[T]
    total: int
    page: int
    size: int

    model_config = ConfigDict(
        from_attributes=True,
    )

    @computed_field
    @property
    def pages(self) -> int:
        return ceil(self.total / self.size) if self.size else 0
