# -*- coding: utf-8 -*-
import unittest

from src.gilded_rose import GildedRose
from src.classes.item import Item


class GildedRoseTest(unittest.TestCase):

    def test_aged_brie_item(self):
        items = [Item("Aged Brie", 1, 10), Item("Aged Brie", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(11, items[0].quality)
        self.assertEqual(-1, items[1].sell_in)
        self.assertEqual(12, items[1].quality)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[1].sell_in)
        self.assertEqual(14, items[1].quality)
        gilded_rose.update_quality()
        self.assertEqual(-3, items[1].sell_in)
        self.assertEqual(16, items[1].quality)

    def test_backstage_passes_item(self):
        items = [
            Item("Backstage passes to a TAFKAL80ETC concert", 11, 10),
            Item("Backstage passes to a TAFKAL80ETC concert", 10, 10),
            Item("Backstage passes to a TAFKAL80ETC concert", 6, 10),
            Item("Backstage passes to a TAFKAL80ETC concert", 5, 10),
            Item("Backstage passes to a TAFKAL80ETC concert", 1, 10),
            Item("Backstage passes to a TAFKAL80ETC concert", 0, 10),
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(10, items[0].sell_in)
        self.assertEqual(11, items[0].quality)
        self.assertEqual(9, items[1].sell_in)
        self.assertEqual(12, items[1].quality)
        self.assertEqual(5, items[2].sell_in)
        self.assertEqual(12, items[2].quality)
        self.assertEqual(4, items[3].sell_in)
        self.assertEqual(13, items[3].quality)
        self.assertEqual(0, items[4].sell_in)
        self.assertEqual(13, items[4].quality)
        self.assertEqual(-1, items[5].sell_in)
        self.assertEqual(0, items[5].quality)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[5].sell_in)
        self.assertEqual(0, items[5].quality)
        gilded_rose.update_quality()
        self.assertEqual(-3, items[5].sell_in)
        self.assertEqual(0, items[5].quality)

    def test_conjured_mana_cacke_item(self):
        items = [Item("Conjured Mana Cake", 1, 10), Item("Conjured Mana Cake", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(8, items[0].quality)
        self.assertEqual(-1, items[1].sell_in)
        self.assertEqual(6, items[1].quality)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[1].sell_in)
        self.assertEqual(2, items[1].quality)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(0, items[1].quality)

    def test_normal_item(self):
        items = [Item("normal", 1, 10), Item("normal", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(9, items[0].quality)
        self.assertEqual(-1, items[1].sell_in)
        self.assertEqual(8, items[1].quality)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[1].sell_in)
        self.assertEqual(6, items[1].quality)
        gilded_rose.update_quality()
        self.assertEqual(-3, items[1].sell_in)
        self.assertEqual(4, items[1].quality)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(0, items[1].quality)

    def test_sulfuras_item(self):
        items = [
            Item("Sulfuras, Hand of Ragnaros", 1, 80),
            Item("Sulfuras, Hand of Ragnaros", 0, 80),
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(80, items[0].quality)
        self.assertEqual(0, items[1].sell_in)
        self.assertEqual(80, items[1].quality)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(80, items[0].quality)
        self.assertEqual(0, items[1].sell_in)
        self.assertEqual(80, items[1].quality)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(80, items[0].quality)
        self.assertEqual(0, items[1].sell_in)
        self.assertEqual(80, items[1].quality)

    def test_quality_upper_limit(self):
        items = [
            Item("Backstage passes to a TAFKAL80ETC concert", 11, 50),
            Item("Backstage passes to a TAFKAL80ETC concert", 6, 49),
            Item("Backstage passes to a TAFKAL80ETC concert", 1, 49),
            Item("Aged Brie", 10, 50),
            Item("Aged Brie", 0, 49),
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
        self.assertEqual(50, items[1].quality)
        self.assertEqual(50, items[2].quality)
        self.assertEqual(50, items[3].quality)
        self.assertEqual(50, items[4].quality)

    def test_quality_lower_limit(self):
        items = [
            Item("normal", 1, 0),
            Item("Conjured Mana Cake", 1, 0),
            Item("Conjured Mana Cake", 0, 1),
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(0, items[1].quality)
        self.assertEqual(0, items[2].quality)


if __name__ == "__main__":
    unittest.main()
