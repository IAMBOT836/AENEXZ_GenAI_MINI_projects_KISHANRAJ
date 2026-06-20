def add_item(item, cart=[]):
    cart.append(item)
    return cart

print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", cart=["bread"]))
print(add_item("eggs"))

#Because the default list cart=[] is created only once when the function is defined. Every call without a cart uses the same list.

def add_item(item, cart=None):
    if cart is None:
        cart = []

    cart.append(item)
    return cart



