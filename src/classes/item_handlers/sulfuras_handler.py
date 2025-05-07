from ..item_registry import DEFAULT_REGISTRY
from ..base.item_handler_base import ItemHandlerBase


@DEFAULT_REGISTRY.register
class SulfurasHandler(ItemHandlerBase):
    @staticmethod
    def should_handle(item):
        return item.name == "Sulfuras, Hand of Ragnaros"

    def update_sell_in(self):
        return

    def update_quality(self):
        return
