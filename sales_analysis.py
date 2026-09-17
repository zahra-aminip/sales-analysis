import pandas as pd
import matplotlib.pylab as plt


df = pd.read_excel("sales_data.xlsx")
# ------------------------ Data cleaning &  -----------------------
print("head values:" ,df.head())
print("\ndescribe values:" ,df.describe())
print("\nData info:")
df.info()
print("\nshape values:" ,df.shape)
print("\nmissing values:", df.isnull().sum())
print("\nduplicated values:", df.duplicated().sum())

df["Date"] =  pd.to_datetime(df["Date"])
print(df.dtypes)

print("Quantity <=0:", (df["Quantity"]<= 0).sum())
print("Sales <=0:", (df["Sales"]<= 0).sum())
print("Cost <=0:", (df["Cost"]<= 0).sum())
print("Discount < 0:", (df["Discount"]< 0).sum())
print("Discount > 100:", (df["Discount"] > 100).sum())

# ----------------------------- creat kpi  ----------------------------

df["Profit"]= df["Sales"]-df["Cost"]
print(df[["Sales", "Cost", "Profit"]].head())

df["Profit Margin"] = (df["Profit"]/df["Sales"])*100
print(df[["Sales", "Cost", "Profit","Profit Margin"]].head())

overall_aov = df["Sales"].mean()
print("Overall Average Order Value:", overall_aov)

#--------------------------------- sales by time-----------------------------
Product_Sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
print("Product_Sales",Product_Sales)

category_sales = df.groupby("Category")[["Sales","Profit","Cost"]].sum()
print("category_sales", category_sales)

df["Month"] = df["Date"].dt.month

monthly_analysis = df.groupby("Month").agg(
    Total_Sales =("Sales" , "sum"),
    Total_Orders = ("OrderID" , "count"),
    Total_Profit = ("Profit","sum")
)
print("monthly_analysis" , monthly_analysis)

city_analysis = df.groupby("City").agg(
    Total_Sales =("Sales" , "sum"),
    Total_Orders = ("OrderID" , "count"),
    Total_Profit = ("Profit","sum")
).sort_values("Total_Sales", ascending= False)
print("city_analysis" , city_analysis)



city_Aov = df.groupby("City").agg(
    Average_Order_Value = ("Sales" , "mean"),
    Total_Orders =("OrderID" , "count"),
    Total_Sales =("Sales" , "sum")
).sort_values("Average_Order_Value" , ascending=False)

print("city_Aov" , city_Aov)

#--------------------------------------------------------------------
city_product_sale = df.pivot_table(
    index="City",
    columns="Product",
    values="Sales",
    aggfunc="sum",
    fill_value=0
)

print("city_product_sale",city_product_sale)
#--------------------------------------------------------------------

city_product_orders = df.pivot_table(
    index="City",
    columns="Product",
    values="OrderID",
    aggfunc="count",
    fill_value=0
)

print("city_product_orders",city_product_orders)
#--------------------------------------------------------------------

city_product_mix = city_product_orders.div(
    city_product_orders.sum(axis=1),
    axis=0
) * 100

print("city_product_mix", city_product_mix.round(2))

#--------------------------------------------------------------------


product_profitability = df.groupby("Product").agg(
    Total_Sales =("Sales" , "sum"),
    Total_Cost =("Cost" , "sum"),
    Total_Profit= ("Profit" , "sum")
)

product_profitability["Profit_Margin"] = (product_profitability["Total_Profit"]/ product_profitability["Total_Sales"]) * 100

product_profitability = product_profitability.sort_values(
    "Total_Profit", ascending=False
)
print("product_profitability", product_profitability.round(2))

#--------------------------------------------------------------------

city_product_profitability = df.groupby(["City", "Product"]).agg(
    Total_Sales = ("Sales","sum"),
    Total_Cost = ("Cost","sum"),
    Total_Profit = ("Profit","sum"),
)

city_product_profitability["Profit_Margin"] = (city_product_profitability["Total_Profit"]/ city_product_profitability["Total_Sales"]) * 100
print("city_product_profitability", city_product_profitability.round(2))


#----------------------------------customer_analysis ----------------------------------
customer_analysis = df.groupby("Customer").agg(
    Total_Sales = ("Sales","sum"),
    Total_Profit = ("Profit","sum"),
    Total_Orders = ("OrderID", "count")
)

customer_analysis["Average_Order_Value"] = customer_analysis["Total_Sales"] /customer_analysis["Total_Orders"]  


customer_analysis = customer_analysis.sort_values("Total_Sales", ascending=False)
print("customer_analysis",customer_analysis)

#----------------------------------Discount_analysis ----------------------------------
discount_analysis = df.groupby("Discount").agg(
    Total_Sales = ("Sales","sum"),
    Total_Profit = ("Profit","sum"),
    Total_Orders = ("OrderID", "count")

).sort_index()

discount_analysis["Profit_Margin"] = (discount_analysis["Total_Profit"]/ discount_analysis["Total_Sales"]) * 100

print("discount_analysis",discount_analysis)



#----------------------------------Visualization ----------------------------------
# design charts
plt.rcParams["figure.facecolor"] = "#F7F8FA"
plt.rcParams["axes.facecolor"] = "white"

plt.rcParams["axes.edgecolor"] = "#D9DDE3"
plt.rcParams["axes.linewidth"] = 1

plt.rcParams["axes.grid"] = True
plt.rcParams["grid.alpha"] = 0.25

plt.rcParams["font.size"] = 10
plt.rcParams["axes.titlesize"] = 14
plt.rcParams["axes.labelsize"] = 11

fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle("Sales Analysis Dashboard",fontsize=18)


# فروش در طول ماه‌های مختلف چه روندی داشته است؟
axes[0, 0].plot( monthly_analysis.index,monthly_analysis["Total_Sales"],marker="o")
axes[0, 0].set_title("Monthly Sales Trend")
axes[0, 0].set_xlabel("Month")
axes[0, 0].set_ylabel("Total Sales")
month_names = ["January", "February", "March", "April", "May", "June"]
axes[0, 0].set_xticks(monthly_analysis.index)
axes[0, 0].set_xticklabels(month_names)
axes[0, 0].ticklabel_format(style="plain", axis="y")
axes[0, 0].grid(axis="y", alpha=0.25)

#کدام شهرها بیشترین فروش را ایجاد کرده‌اند؟
axes[0, 1].bar(city_analysis.index, city_analysis["Total_Sales"])
axes[0, 1].set_title("Sales by City")
axes[0, 1].set_xlabel("City")
axes[0, 1].set_ylabel("Total Sales")
axes[0, 1].ticklabel_format(style="plain",axis="y")
axes[0, 1].grid( axis="y",alpha=0.25)

#کدام محصولات بیشترین فروش را ایجاد کرده‌اند؟
axes[0, 2].bar( Product_Sales.index, Product_Sales.values)
axes[0, 2].set_title("Sales by Product")
axes[0, 2].set_xlabel("Product")
axes[0, 2].set_ylabel("Total Sales")
axes[0, 2].ticklabel_format(style="plain",axis="y")
axes[0, 2].grid(axis="y", alpha=0.25)

#کدام محصول بیشترین سود ایجاد می‌کند و حاشیه سود هر محصول چقدر است؟
axes[1, 0].bar( product_profitability.index,product_profitability["Total_Profit"])
axes[1, 0].set_title("Total Profit by Product")
axes[1, 0].set_xlabel("Product")
axes[1, 0].set_ylabel("Total Profit")
axes[1, 0].ticklabel_format(style="plain",axis="y")
axes[1, 0].grid( axis="y",alpha=0.25)

#Top 10 Customers by Sales
top_10_customers = customer_analysis.sort_values( "Total_Sales",ascending=False).head(10)
axes[1, 1].bar(top_10_customers.index,top_10_customers["Total_Sales"])
axes[1, 1].set_title("Top 10 Customers by Sales")
axes[1, 1].set_xlabel("Customer")
axes[1, 1].set_ylabel("Total Sales")
axes[1, 1].ticklabel_format( style="plain",  axis="y")
axes[1, 1].tick_params(axis="x", rotation=45)
axes[1, 1].grid( axis="y",alpha=0.25)

#Profit Margin by Discount
axes[1, 2].bar( discount_analysis.index.astype(str),discount_analysis["Profit_Margin"])
axes[1, 2].set_title("Profit Margin by Discount")
axes[1, 2].set_xlabel("Discount (%)")
axes[1, 2].set_ylabel("Profit Margin (%)")
axes[1, 2].grid(axis="y", alpha=0.25)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("outputs/charts/sales_dashboard.png", dpi=300)
plt.show()




# فروش در طول ماه‌های مختلف چه روندی داشته است؟
# plt.plot(monthly_analysis.index, monthly_analysis["Total_Sales"], marker = "o")
# plt.title("Monthly Sales Trend")
# plt.xlabel("Month")
# plt.ylabel("Total Sales")
# month_names = ["January", "February", "March", "April", "May", "June"]
# plt.xticks(monthly_analysis.index,month_names)
# plt.ticklabel_format(style="plain", axis="y")
# plt.tight_layout()
# plt.show()

#کدام شهرها بیشترین فروش را ایجاد کرده‌اند؟
# plt.figure(figsize=(10,5))
# plt.bar( city_analysis.index, city_analysis["Total_Sales"])
# plt.title("Sales by City")
# plt.xlabel("City")
# plt.ylabel("Total Sales")
# plt.ticklabel_format(style="plain", axis="y")
# plt.tight_layout()
# plt.show()

#کدام محصولات بیشترین فروش را ایجاد کرده‌اند؟
# plt.figure(figsize=(10,5))
# plt.bar(Product_Sales.index,Product_Sales.values)
# plt.title("Sales by Product")
# plt.xlabel("Product")
# plt.ylabel("Total Sales")
# plt.ticklabel_format(style="plain", axis="y")
# plt.tight_layout()
# plt.show()

#کدام محصول بیشترین سود ایجاد می‌کند و حاشیه سود هر محصول چقدر است؟

# plt.figure(figsize=(10, 5))
# plt.bar( product_profitability.index,product_profitability["Total_Profit"])
# plt.title("Total Profit by Product")
# plt.xlabel("Product")
# plt.ylabel("Total Profit")
# plt.ticklabel_format(style="plain", axis="y")
# plt.tight_layout()
# plt.show()

#Top 10 Customers by Sales
# top_customers = customer_analysis.sort_values( "Total_Sales",ascending=False).head(10)
# plt.figure(figsize=(10,5))
# plt.bar( top_customers.index,top_customers["Total_Sales"])
# plt.title("Top 10 Customers by Sales")
# plt.xlabel("Customer")
# plt.ylabel("Total Sales")
# plt.ticklabel_format(style="plain", axis="y")
# plt.xticks(rotation=45, ha="right")
# plt.tight_layout()
# plt.show()

#Profit Margin by Discount
# plt.figure(figsize=(10,5))
# plt.bar( discount_analysis.index.astype(str),discount_analysis["Profit_Margin"])
# plt.title("Profit Margin by Discount")
# plt.xlabel("Discount (%)")
# plt.ylabel("Profit Margin (%)")
# plt.tight_layout()
# plt.show()
