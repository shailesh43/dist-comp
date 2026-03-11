# ---------------- STATEFUL SYSTEM ----------------
# Example: Shopping cart that remembers previously added items

cart = []   # Global state (memory)

def stateful(item):
    cart.append(item)
    return f"Stateful Cart: {cart}"

n = int(input("Enter number of items to add to stateful cart: "))

for i in range(n):
    item = input("Enter item name: ")
    print(stateful(item))


# ---------------- STATELESS SYSTEM ----------------
# Example: System does not remember previous items

def stateless(item):
    cart = []      # Local variable (resets every time)
    cart.append(item)
    return f"Stateless Cart: {cart}"

n = int(input("\nEnter number of items for stateless cart: "))

for i in range(n):
    item = input("Enter item name: ")
    print(stateless(item))