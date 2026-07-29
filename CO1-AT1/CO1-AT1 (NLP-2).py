import re

# Product List
products = [
    "Laptop",
    "Laptop Stand",
    "Wireless Mouse",
    "Gaming Mouse",
    "Bluetooth Speaker",
    "Smart Watch",
    "Phone Case",
    "Coffee Maker",
    "Java Programming Book",
    "Python Programming Book"
]

# Exact Search
exact = "Laptop"
exact_match = [p for p in products if re.fullmatch(exact, p)]

# Prefix Search
prefix = "Lap"
prefix_match = [p for p in products if re.match(prefix, p)]

# Suffix Search
suffix = "Book"
suffix_match = [p for p in products if re.search(suffix + r"$", p)]

# Partial Search
partial = "Mouse"
partial_match = [p for p in products if re.search(partial, p)]

# Case-Insensitive Search
case = "pYtHoN"
case_match = [p for p in products if re.search(case, p, re.IGNORECASE)]

# Display Results
print("Exact Search:", exact)
print(exact_match)
print("Total Matches:", len(exact_match))

print("\nPrefix Search:", prefix)
print(prefix_match)
print("Total Matches:", len(prefix_match))

print("\nSuffix Search:", suffix)
print(suffix_match)
print("Total Matches:", len(suffix_match))

print("\nPartial Search:", partial)
print(partial_match)
print("Total Matches:", len(partial_match))

print("\nCase-Insensitive Search:", case)
print(case_match)
print("Total Matches:", len(case_match))
