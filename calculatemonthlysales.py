import matplotlib.pyplot as plt

salesData = [
    {"productID": "P001", "quantity": 5, "month": "Jan"},
    {"productID": "P002", "quantity": 3, "month": "Jan"},
    {"productID": "P001", "quantity": 2, "month": "Jan"},
    {"productID": "P003", "quantity": 4, "month": "Jan"},
]

monthlySales = {}

for sale in salesData:
    monthlySales[sale["productID"]] = monthlySales.get(sale["productID"], 0) + sale["quantity"]

print("Monthly Sales per Product:")
for product, total in monthlySales.items():
    print(f"{product}: {total}")

products = list(monthlySales.keys())
totals = list(monthlySales.values())

plt.figure(figsize=(6,4))
plt.bar(products, totals, color=['#3B82F6', '#6366F1', '#2563EB'])
plt.title("Monthly Sales per Product")
plt.xlabel("Product ID")
plt.ylabel("Total Sales")
plt.show()ext=(0, 3), textcoords="offset points", ha="center", va="bottom", fontsize=9)

plt.tight_layout()
plt.savefig("monthly_sales.png", dpi=150)  # optional: saves the figure
plt.show()
