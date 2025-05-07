# -*- coding: utf-8 -*-
from abc import ABC as AbstractClass, abstractmethod
from typing import Self, Type


class ItemHandler(AbstractClass):
    def __init__(self, item: "Item"):
        self._item = item

    @property
    def item(self) -> "Item":
        return self._item

    def adjust_quality(self, delta: int):
        MAX_QUALITY = 50
        MIN_QUALITY = 0

        self._item.quality = min(MAX_QUALITY, max(MIN_QUALITY, self._item.quality + delta))

    @staticmethod
    @abstractmethod
    def should_handle(item: "Item") -> bool: ...

    @abstractmethod
    def update_sell_in(self) -> None: ...

    @abstractmethod
    def update_quality(self) -> None: ...

class ItemHandlerRegistry:
    def __init__(self: Self, fallback: Type["ItemHandler"] | None = None):
        self._registry: list[ItemHandler] = []
        self._fallback = fallback

    def register(self, handler: Type[ItemHandler]) -> Type[ItemHandler]:
        if handler is not self._fallback:
            self._registry.append(handler)
        return handler
    
    def get_handler(self, item: Type["Item"]):
        for handler in self._registry:
            if handler.should_handle(item):
                return handler(item)
        return self._fallback(item)

class NormalHandler(ItemHandler):
    @staticmethod
    def should_handle():
        return True

    def update_sell_in(self):
        self._item.sell_in -= 1
        

    def update_quality(self):
        # 一般物品的過期後品質更新邏輯
        if self._item.sell_in < 0:
            self.adjust_quality(-2)
        # 一般物品的品質更新邏輯
        else:
            self.adjust_quality(-1)

handler_registry = ItemHandlerRegistry(NormalHandler)

@handler_registry.register
class SulfurasHandler(ItemHandler):
    @staticmethod
    def should_handle(item):
        return item.name == "Sulfuras, Hand of Ragnaros"

    def update_sell_in(self):
        return

    def update_quality(self):
        return

@handler_registry.register
class AgedBrieHandler(ItemHandler):
    @staticmethod
    def should_handle(item):
        return item.name == "Aged Brie"

    def update_sell_in(self):
        self._item.sell_in -= 1

    def update_quality(self):
        # Aged Brie 的過期後品質更新邏輯
        if self._item.sell_in < 0:
            self.adjust_quality(2)
        # Aged Brie 的品質更新邏輯
        else:
            self.adjust_quality(1)

@handler_registry.register
class BackstagePassHandler(ItemHandler):
    @staticmethod
    def should_handle(item):
        return item.name == "Backstage passes to a TAFKAL80ETC concert"

    def update_sell_in(self):
        self._item.sell_in -= 1

    def update_quality(self):
        # Backstage passes to a TAFKAL80ETC concert 的品質更新邏輯
        if self._item.sell_in >= 10:
            self.adjust_quality(1)
        elif self._item.sell_in < 10 and self._item.sell_in >= 5:
            self.adjust_quality(2)
        elif self._item.sell_in < 5 and self._item.sell_in >= 0:
            self.adjust_quality(3)
        # Backstage passes to a TAFKAL80ETC concert 的過期後品質更新邏輯
        else:
            self._item.quality = 0

class GildedRose(object):
    def __init__(self, items):
        self._handlers = [handler_registry.get_handler(item) for item in items]

    def update_quality(self):
        for handler in self._handlers:
            handler.update_sell_in()
            handler.update_quality()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)