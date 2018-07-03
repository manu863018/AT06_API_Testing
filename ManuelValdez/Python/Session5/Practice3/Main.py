from Picker import Picker
from CheckOut import CheckOut
from Items import printInitialData



picker = Picker()
picker.fillIntoBuyingCart(1, 3)
picker.fillIntoBuyingCart(2, 2)
picker.fillIntoBuyingCart(3, 5)
picker.fillIntoBuyingCart(3, 1)
picker.printBuyingCart()

checkOut = CheckOut(picker.getBuyingCart())
checkOut.purchase()
checkOut.printPurchase()

printInitialData()