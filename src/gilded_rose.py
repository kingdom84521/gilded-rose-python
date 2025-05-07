# -*- coding: utf-8 -*-
from .classes.item_registry import DEFAULT_REGISTRY
from .classes import item_handlers

_unused_import = item_handlers


class GildedRose(object):
    def __init__(self, items):
        self._handlers = [DEFAULT_REGISTRY.get_handler(item) for item in items]

    def update_quality(self):
        for handler in self._handlers:
            if handler:
                handler.update_sell_in()
                handler.update_quality()
