class ShoppingCart(object):
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items_in_cart = {}
    def add_item(self, product, price):
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print product + " added."
        else:
            print product + " is already in the cart."
    def remove_item(self, product):
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print product + " removed."
        else:
            print product + " is not in the cart."
    def sum_cart(self):
        sum = 0
        for i in self.items_in_cart:
            sum += self.items_in_cart[i]
        return sum

my_cart = ShoppingCart("dima")
my_cart.add_item("socks", 10)
my_cart.add_item("bread", 2)
print my_cart.items_in_cart
print len(my_cart.items_in_cart)
print my_cart.sum_cart()