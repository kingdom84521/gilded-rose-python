from ..base.item_handler_base import ItemHandlerBase
from ..item_registry import DEFAULT_REGISTRY


@DEFAULT_REGISTRY.register
class AgedBrieHandler(ItemHandlerBase):
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
