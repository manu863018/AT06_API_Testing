from Items import initialData
from Log import Log

class CheckOut:

    def __init__(self, buyingCart):
        self.buyingCart = buyingCart
        self.logger = Log()


    def purchase(self):
        log = self.logger.initLog()
        log.info("Calculate Total")
        total = 0
        for item in self.buyingCart:
            log.debug("Total for item:" + str(item))
            total += initialData[item]["price"] * self.buyingCart[item]
            initialData[item]["amount"] = initialData[item]["amount"] - self.buyingCart[item]
        print("Total:", total)

    def printPurchase(self):
        log = self.logger.initLog()
        log.info("Print purchase")
        print("Item | Price | Amount")
        for item in self.buyingCart:
            log.debug("item" + str(item))
            print("{} | {} | {}".format(initialData[item]["name"], initialData[item]["price"], self.buyingCart[item]))