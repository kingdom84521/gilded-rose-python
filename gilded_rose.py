# -*- coding: utf-8 -*-


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_item_sell_in(self, item):
        # Sulfuras, Hand of Ragnaros 是 Special Case, 略過
        if item.name == "Sulfuras, Hand of Ragnaros":
            return

        item.sell_in = item.sell_in - 1

    def update_item_quality(self, item):
        # Sulfuras, Hand of Ragnaros 是 Special Case, 略過
        if item.name == "Sulfuras, Hand of Ragnaros":
            return

        # sell_in 會影響 quality 更新邏輯的物品的更新邏輯 (Aged Brie 和 Backstage passes to a TAFKAL80ETC concert)
        if item.name == "Aged Brie":
            # Aged Brie 的過期後品質更新邏輯
            if item.sell_in < 0:
                item.quality = item.quality + 2
            # Aged Brie 的品質更新邏輯
            else:
                item.quality = item.quality + 1
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
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
        else:
            if item.sell_in < 0:
                item.quality = item.quality - 2
            # 一般物品的品質更新邏輯
            else:
                item.quality = item.quality - 1

        # 物品品質(quality)不得超過 50
        if item.quality > 50:
            item.quality = 50
        # 物品品質(quality)不得少於 0
        if item.quality < 0:
            item.quality = 0

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
