from ..base.item_handler_base import ItemHandlerBase
from ..item_registry import DEFAULT_REGISTRY


@DEFAULT_REGISTRY.register
class BackstagePassesHandler(ItemHandlerBase):
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
