salesData = [
    {"productID": "P1", "quantity": 5, "month": "Jan"},
    {"productID": "P2", "quantity": 3, "month": "Jan"},
    {"productID": "P1", "quantity": 2, "month": "Jan"},
    {"productID": "P3", "quantity": 4, "month": "Jan"},
]

monthlySales = {}

for sale in salesData:
    monthlySales[sale["productID"]] = monthlySales.get(sale["productID"], 0) + sale["quantity"]

print("Monthly Sales per Product:")
for product, total in monthlySales.items():
    print(f"{product}: {total}")
