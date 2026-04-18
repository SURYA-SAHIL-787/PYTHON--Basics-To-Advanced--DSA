# ecommerce_sort.py

"""
Real-world application: E-Commerce Product Listing Sorter
Bubble sort arranges products by customer rating (highest first)
so shoppers see the best-rated items at the top of search results.
"""


def bubble_sort_products(products):
    n = len(products)
    for pass_num in range(n - 1):
        swapped = False
        for i in range(n - 1 - pass_num):
            if products[i]["rating"] < products[i + 1]["rating"]:
                products[i], products[i + 1] = products[i + 1], products[i]
                swapped = True
        if not swapped:
            break
    return products


def display_products(products, title="Product Listing"):
    print(f"\n{'─' * 65}")
    print(f"  {title}")
    print(f"{'─' * 65}")
    print(f"  {'#':<5} {'Product':<25} {'Category':<18} {'Price':>8}  {'Rating'}")
    print(f"  {'─'*4:<5} {'─'*23:<25} {'─'*16:<18} {'─'*7:>8}  {'─'*6}")
    for rank, p in enumerate(products, 1):
        r = p["rating"]
        color = "\033[92m" if r >= 4.5 else "\033[93m" if r >= 3.5 else "\033[91m"
        reset = "\033[0m"
        stars = "★" * int(r) + "☆" * (5 - int(r))
        print(f"  {color}#{rank:<4}{reset} {p['name']:<25} {p['category']:<18}"
              f" ₹{p['price']:>7,}  {color}{r} {stars}{reset}")
    print(f"{'─' * 65}\n")


def main():
    products = [
        {"name": "boAt Rockerz 450",   "category": "Headphones",  "price": 1499,  "rating": 4.2},
        {"name": "Samsung 55\" QLED",  "category": "Television",  "price": 74999, "rating": 4.7},
        {"name": "Prestige Mixer",      "category": "Kitchen",     "price": 2999,  "rating": 3.8},
        {"name": "OnePlus Nord CE 3",   "category": "Smartphone",  "price": 24999, "rating": 4.5},
        {"name": "Wildcraft Backpack",  "category": "Bags",        "price": 1799,  "rating": 3.2},
        {"name": "Kindle Paperwhite",   "category": "E-Reader",    "price": 13999, "rating": 4.6},
        {"name": "Philips Air Fryer",   "category": "Kitchen",     "price": 6499,  "rating": 4.1},
        {"name": "Noise ColorFit Pro",  "category": "Smartwatch",  "price": 3499,  "rating": 3.9},
        {"name": "HP Wireless Mouse",   "category": "Accessories", "price": 599,   "rating": 4.8},
        {"name": "Bajaj Tower Fan",     "category": "Appliances",  "price": 2199,  "rating": 2.9},
    ]

    print("\n🛒  E-Commerce Product Listing Sorter")
    print("    Bubble Sort — showing best-rated products first\n")

    display_products(products, title="Default Listing (unsorted)")

    sorted_products = bubble_sort_products(products.copy())

    display_products(sorted_products, title="Sorted by Rating — Best First")

    top = sorted_products[0]
    print(f"  🏆  Top pick: \033[92m{top['name']}\033[0m"
          f" — ₹{top['price']:,} | Rating {top['rating']}/5.0\n")


if __name__ == "__main__":
    main()
