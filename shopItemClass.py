from images import *
from plantClass import *

class shopItem():

    def __init__(self, name, image, inStock, cost, type, item):

        self.name = name
        self.image = image
        self.inStock = inStock
        self.cost = cost
        self.type = type
        self.item = item


#plant
#item
#fertilizer
#measurement
#skill

itemNet = shopItem('Plant Net', itemEmpty, 10, 50, 'item', None)

fertilizerSmall = shopItem('Small Fertilizer', itemEmpty, 5, 100, 'fertilizer', None)
fertilizerMid = shopItem('Mid Fertilizer', itemEmpty, 3, 200, 'fertilizer', None)
fertilizerBig = shopItem('Big Fertilizer', itemEmpty, 1, 300, 'fertilizer', None)

plantBasic = shopItem('Basic Plant', plant4, 4, 100, 'plant', None)