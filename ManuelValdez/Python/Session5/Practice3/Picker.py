from Items import initialData


class Picker:

    def __init__(self):
        self.buyingCart = {}


    def fillIntoBuyingCart(self, itemId, amount):
        if itemId in self.buyingCart:
            self.buyingCart[itemId] = self.buyingCart[itemId] + amount
        else:
            self.buyingCart[itemId] = amount


    def printBuyingCart(self):
        for id in self.buyingCart:
            print("Item:", id, ", Name:", initialData[id]["name"], ", Price:", initialData[id]["price"], ", Amount", self.buyingCart[id])


    def getBuyingCart(self):
        return self.buyingCart