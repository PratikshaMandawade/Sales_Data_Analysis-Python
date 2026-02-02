import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('Sales_Data.csv')

#create Revenue column
data["Revenue"] = data["Quantity"] * data["Price"]
print(data)
print("\nTotal Revenue:",data ["Revenue"].sum())

#City-wise total revenue
city_revenue= data.groupby("City")["Revenue"].sum()
print(city_revenue)

#Best-selling product(by Quantity)
product_sales=data.groupby("Product")["Quantity"].sum()
print("\nProduct-wise Quantity Sold:")
print(product_sales)

#Monthly Sales Trend
data["Order_Date"]=pd.to_datetime(data["Order_Date"])
data["Month"]=data["Order_Date"].dt.month
monthly_sales=data.groupby("Month")["Revenue"].sum()
print("\nMonthly Sales:")
print(monthly_sales)

# Product-wise quantity sold
product_quantity = data.groupby("Product")["Quantity"].sum().sort_values(ascending=False)
print("\nProduct-wise Quantity Sold:")
print(product_quantity)

# Best-selling product
best_Selling_product=product_quantity.idxmax()
best_quantity=product_quantity.max()
print("\nBest Salling Product:")
print(best_Selling_product,"With quantity",best_quantity)

#Product-wise Revenue Analysis
product_revenue=(data.groupby("Product")["Revenue"].sum().sort_values(ascending=False))
print("\nProduct-wise Revenue(Desending order):")
print(product_revenue)

#Highest revenue product
top_revenue_product=product_revenue.index[0]
top_revenue_value=product_revenue.iloc[0]
print("\nHighest Revenue Product:")
print(top_revenue_product,"With quantity",top_revenue_value)

# Product-wise Revenue Bar Chart
import matplotlib.pyplot as plt
# Bar chart for product-wise revenue
product_revenue.plot(kind="bar")
plt.title("Product-wise Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()

plt.show()
#Convert Order_Date to datetime
data["Order_Date"]=pd.to_datetime(data["Order_Date"])

#Extract month name
data["Month"]=data["Order_Date"].dt.month_name

#Monthly revenue
monthly_revenue=data.groupby("Month")["Revenue"].sum()
print("\nMonthly Revenue:")
print(monthly_revenue)

#Line graph for monthly revenue
monthly_revenue.plot(kind="line",marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)
plt.tight_layout()
plt.show()

