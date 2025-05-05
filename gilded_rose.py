# -*- coding: utf-8 -*-


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            # Sulfuras, Hand of Ragnaros 是 Special Case, 略過
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            # 不需要在乎 sell_in 和 quality 的關係的物品的更新邏輯
            if (
                item.name != "Aged Brie"
                and item.name != "Backstage passes to a TAFKAL80ETC concert"
            ):
                if item.quality > 0:
                    item.quality = item.quality - 1
            # sell_in 會影響 quality 更新邏輯的物品的更新邏輯 (Aged Brie 和 Backstage passes to a TAFKAL80ETC concert)
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    # Backstage passes to a TAFKAL80ETC concert 的品質更新邏輯
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            item.sell_in = item.sell_in - 1
            # 過期後的各類物品的品質更新邏輯
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        # 一般物品的過期後品質更新邏輯
                        if item.quality > 0:
                            item.quality = item.quality - 1
                    # Backstage passes to a TAFKAL80ETC concert 的過期後品質更新邏輯
                    else:
                        item.quality = item.quality - item.quality
                # Aged Brie 的過期後品質更新邏輯
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
