
# 1. I'd use bracket notation (customer["name"]) when a key is required, like a
#    customer ID, because a KeyError tells me right away that the data is bad.
#    I'd use .get("key", default) when a key is optional or might be missing,
#    like an email or discount code, so the program keeps running with a safe
#    default. My rule of thumb: brackets for required data, .get() for optional.
#
# 2. Building a summary dictionary is like a SUMIF formula or a PivotTable in
#    Excel: group rows by a category and total a value. The Python version is
#    better for large datasets because it handles millions of rows without
#    slowing down or hitting Excel's row limit, and the same script can be
#    rerun on new data instantly instead of rebuilding formulas by hand.


# ---------- Exercise 1: One customer ----------
print("=== Exercise 1 ===")
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250.00,
}

print("Name:", customer["name"])
print("Email:", customer["email"])
print("Tier:", customer["tier"])
print("YTD spend:", customer["ytd_spend"])
print(customer)


# ---------- Exercise 2: Update and add ----------
print("\n=== Exercise 2 ===")
customer["phone"] = "813-555-0142"
print("After adding phone:", customer)

customer["tier"] = "platinum"
print("After upgrading tier:", customer)

del customer["email"]
print("After deleting email:", customer)


# ---------- Exercise 3: Safe lookup ----------
print("\n=== Exercise 3 ===")
print("Using .get():", customer.get("email", "no email on file"))

try:
    print("Using brackets:", customer["email"])
except KeyError:
    print("Using brackets: KeyError - 'email' is not in the dictionary")


# ---------- Exercise 4: Iterate ----------
print("\n=== Exercise 4 ===")
for key, value in customer.items():
    print(f"{key}: {value}")

print("-- without .items() --")
for key in customer:
    print(key)
# Looping over a dictionary directly only gives you the keys.
# .items() gives you each key AND its value together, so you don't
# have to look up customer[key] separately.


# ---------- Exercise 5: Lookup table ----------
print("\n=== Exercise 5 ===")
tier_discounts = {"bronze": 0, "silver": .05, "gold": .10, "platinum": .15}

purchase = 200
rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - rate)

print(f"Tier: {customer['tier']}")
print(f"Discount rate: {rate:.0%}")
print(f"Final price on ${purchase}: ${final_price:.2f}")


# ---------- Exercise 6: List of dicts ----------
print("\n=== Exercise 6 ===")
customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Ben", "tier": "gold"},
    {"name": "Carla", "tier": "silver"},
    {"name": "Dev", "tier": "bronze"},
]

purchase = 300
for c in customers:
    discount = purchase * tier_discounts.get(c["tier"], 0)
    print(f"{c['name']:<6} | {c['tier']:<8} | discount on ${purchase}: ${discount:.2f}")


# ---------- Exercise 7: Nested catalog ----------
print("\n=== Exercise 7 ===")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product, info in catalog.items():
    if info["stock"] < 20:
        print(f"LOW STOCK: {product} has only {info['stock']} units left")


# ---------- Exercise 8: Sales by region ----------
print("\n=== Exercise 8 ===")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]

summary = {}
for t in transactions:
    region = t["region"]
    summary[region] = summary.get(region, 0) + t["amount"]

for region in sorted(summary):
    print(f"{region}: {summary[region]}")
