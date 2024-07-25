# Write a function to calculate the total price of items in a shopping cart.
# Use positional-only arguments for item prices.
# Use a keyword argument for the tax rate with a default value.
# Return the total price including tax.

# Tarberak 1
def shopping_cart(tax = 0.1, **items):
    sum_items = sum(items.values())
    total = sum_items * (1 + tax)
    return total

result = shopping_cart(apple=10, banana=30, carrot=20)
print(result)

# Tarberak 2
def shopping(*items, tax = 0.05):
    total = sum(items) * (1 + tax)
    return total

res = shopping(10, 20, 30)
print(res)