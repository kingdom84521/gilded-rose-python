from ..base.item_handler_base import ItemHandlerBase
from ..item_registry import DEFAULT_REGISTRY


@DEFAULT_REGISTRY.register
class ConjuredManaCakeHandler(ItemHandlerBase):
    @staticmethod
    def should_handle(item):
        return item.name == "Conjured Mana Cake"

    def update_sell_in(self):
        self._item.sell_in -= 1

    def update_quality(self):
        # 一般物品的過期後品質更新邏輯
        if self._item.sell_in < 0:
            self.adjust_quality(-4)
        # 一般物品的品質更新邏輯
        else:
            self.adjust_quality(-2)
