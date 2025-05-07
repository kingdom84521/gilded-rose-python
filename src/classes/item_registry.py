from .base.item_handler_base import ItemHandlerBase
from .item import Item
from typing import Optional, Type, Self


class ItemHandlerRegistry:
    def __init__(self: Self):
        self._registry: list[Type[ItemHandlerBase]] = []
        self._fallback: Optional[Type[ItemHandlerBase]] = None

    def register(self, handler: Type[ItemHandlerBase]) -> Type[ItemHandlerBase]:
        if handler is not self._fallback:
            self._registry.append(handler)
        return handler

    def register_as_fallback(
        self, handler: Type[ItemHandlerBase]
    ) -> Type[ItemHandlerBase]:
        self._fallback = handler
        return handler

    def get_handler(self, item: "Item"):
        for handler in self._registry:
            if handler.should_handle(item):
                return handler(item)
        return self._fallback(item) if self._fallback else None


DEFAULT_REGISTRY = ItemHandlerRegistry()
