from abc import ABC as AbstractClass, abstractmethod
from ..item import Item


class ItemHandlerBase(AbstractClass):
    def __init__(self, item: Item):
        self._item = item

    @property
    def item(self) -> Item:
        return self._item

    def adjust_quality(self, delta: int):
        MAX_QUALITY = 50
        MIN_QUALITY = 0

        self._item.quality = min(
            MAX_QUALITY, max(MIN_QUALITY, self._item.quality + delta)
        )

    @staticmethod
    @abstractmethod
    def should_handle(item: Item) -> bool: ...

    @abstractmethod
    def update_sell_in(self) -> None: ...

    @abstractmethod
    def update_quality(self) -> None: ...
