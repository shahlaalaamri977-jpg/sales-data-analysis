salesData = [
    {"productID": "P10", "quantity": 5, "month": "Jan"},
    {"productID": "P20", "quantity": 3, "month": "Jan"},
    {"productID": "P11", "quantity": 2, "month": "Jan"},
    {"productID": "P34", "quantity": 4, "month": "Jan"},
]

monthlySales = {}

for sale in salesData:
    monthlySales[sale["productID"]] = monthlySales.get(sale["productID"], 0) + sale["quantity"]

print("Monthly Sales per Product:")
for product, total in monthlySales.items():
    print(f"{product}: {total}")
