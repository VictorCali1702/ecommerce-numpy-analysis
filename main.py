#Small Project: Online store order analysis (NumPy + Pandas + Matplotlib)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
os.makedirs("plots", exist_ok=True)

#we set seed for repeatability.
np.random.seed(42)

#number of orders.
num_orders = 100

#Day of order (1-30)
order_day = np.random.randint(1,31, size = num_orders)

#Unit prices from 20 to 500$ (accurate to 2 decimal places)
unit_prices = np.round(np.random.uniform(20, 500, size = num_orders), 2)

#Number of products in the order(1 to 5 quantities)
quantities = np.random.randint(1, 5, size = num_orders)

#Random clients(10 unique IDs)
customer_ids = np.random.choice([f"CUST_{i}" for i in range(1,11)], size = num_orders)

#Creating DataFrame
df = pd.DataFrame({
	"order_day": order_day,
	"customer_id": customer_ids,
	"unit_price": unit_prices,
	"quantity": quantities
})

#We calculate the value of the order.
df["total_value"] = df["unit_price"] * df["quantity"]

#Simple Analysis:
print("Average Order Value:", round(df["total_value"].mean(), 2), "zł") 	#Average Order Value AOV

print("\nTop 10 Most Expensive Orders:")
print(df.sort_values("total_value", ascending = False).head(10), "\n")	#Top 10 most expensive orders

print("Total Value of Orders for Each Day")
print(df.groupby("order_day")["total_value"].sum(), "\n") 	#total value of orders for each day

print("Top 5 Customers by Total Orders")
print(df.groupby("customer_id")["total_value"].sum().sort_values(ascending = False).head(5))

#Graphs/Plots


plt.figure(figsize=(16,10))

#plot1: Summary of orders by month day
plt.subplot(2,2,1)
df.groupby("order_day")["total_value"].sum().plot(kind="bar", color="skyblue")
plt.title("Total value of orders per day")
plt.xlabel("Day of Month")
plt.ylabel("Total Value in PLN")
plt.savefig("plots/orders_by_day.png")

#plot2: Top 5 Customers by total orders
plt.subplot(2,2,2)
df.groupby("customer_id")["total_value"].sum().sort_values(ascending = False).head(5).plot(kind="bar", color = "orange")
plt.title("Top 5 Customers")
plt.xlabel("Customer ID")
plt.ylabel("Shopping Value in PLN")
plt.savefig("plots/top5_customers.png")

#plot3: Histogram Order Value
plt.subplot(2,2,3)
plt.hist(df["total_value"], bins=15, color = "lightgreen", edgecolor= "black")
plt.title("Order Value Distribution")
plt.xlabel("Order Value in PLN")
plt.ylabel("Number of Orders")
plt.savefig("plots/order_value.png")

plt.tight_layout()
plt.show()


