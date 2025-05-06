# -*- coding: utf-8 -*-


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_item_sell_in(self, item):
        # Sulfuras, Hand of Ragnaros 是 Special Case, 略過
        if item.name == "Sulfuras, Hand of Ragnaros":
            return

        item.sell_in = item.sell_in - 1

    def _clamp_quality(self, quality):
        # 限制 quality 的範圍
        return 50 if quality > 50 else 0 if quality < 0 else quality

    def update_sulfuras_quality(self, item):
        # Sulfuras, Hand of Ragnaros 是 Special Case, 略過
        return

    def update_aged_brie_quality(self, item):
        # Aged Brie 的過期後品質更新邏輯
        if item.sell_in < 0:
            item.quality = item.quality + 2
        # Aged Brie 的品質更新邏輯
        else:
            item.quality = item.quality + 1

        item.quality = self._clamp_quality(item.quality)

    def update_backstage_pass_quality(self, item):
        # Backstage passes to a TAFKAL80ETC concert 的品質更新邏輯
        if item.sell_in >= 10:
            item.quality = item.quality + 1
        elif item.sell_in < 10 and item.sell_in >= 5:
            item.quality = item.quality + 2
        elif item.sell_in < 5 and item.sell_in >= 0:
            item.quality = item.quality + 3
        # Backstage passes to a TAFKAL80ETC concert 的過期後品質更新邏輯
        else:
            item.quality = item.quality - item.quality

        item.quality = self._clamp_quality(item.quality)

    def udpate_normal_quality(self, item):
        # 一般物品的過期後品質更新邏輯
        if item.sell_in < 0:
            item.quality = item.quality - 2
        # 一般物品的品質更新邏輯
        else:
            item.quality = item.quality - 1

        item.quality = self._clamp_quality(item.quality)

    def update_item_quality(self, item):
        # Sulfuras, Hand of Ragnaros 是 Special Case, 略過
        if item.name == "Sulfuras, Hand of Ragnaros":
            self.update_sulfuras_quality(item)
        elif item.name == "Aged Brie":
            self.update_aged_brie_quality(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            self.update_backstage_pass_quality(item)
        else:
            self.udpate_normal_quality(item)

    def update_quality(self):
        for item in self.items:
            self.update_item_sell_in(item)
            self.update_item_quality(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
