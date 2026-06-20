def create_cart(owner, discount=0):
    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }


def add_to_cart(cart, name, price, qty=1):
    item = {
        "name": name,
        "price": price,
        "qty": qty
    }

    cart["items"].append(item)


def update_price(price_tuple, new_price):
    try:
        price_tuple[0] = new_price
    except TypeError:
        print("TypeError: Tuples are immutable and cannot be modified.")


def calculate_total(cart):
    total = 0

    for item in cart["items"]:
        total += item["price"] * item["qty"]

    discount_amount = total * (cart["discount"] / 100)

    final_total = total - discount_amount

    return final_total


# Customer 1
cart1 = create_cart("Kishan", 10)

add_to_cart(cart1, "Laptop", 50000, 1)
add_to_cart(cart1, "Mouse", 500, 2)

# Customer 2
cart2 = create_cart("Rahul", 5)

add_to_cart(cart2, "Keyboard", 1500, 1)
add_to_cart(cart2, "Headphones", 2000, 1)

print("Cart 1:")
print(cart1)

print("\nCart 2:")
print(cart2)

print("\nTotal for Cart 1:", calculate_total(cart1))
print("Total for Cart 2:", calculate_total(cart2))

price_info = (50000,)
update_price(price_info, 60000)


# 1. Why is discount=0 safe but cart=[] dangerous?
# discount=0 is immutable. It cannot be changed.
# cart=[] is mutable and gets shared across function calls.

# 2. Difference between rebinding and mutating?
# Rebinding means assigning a new object to a variable.
# Mutating means changing the contents of the existing object.

# Example:
# x = [1,2]
# x = [3,4]  -> Rebinding
# x.append(5) -> Mutating

# 3. Mutable and Immutable Types
# Mutable: list, dict, set
# Immutable: tuple, str, int

# 4. When a list is passed to a function and modified,
# changes reflect outside because both variables
# refer to the same list object in memory.