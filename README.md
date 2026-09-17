# Sales Data Analysis

## Project Overview

This project analyzes sales transaction data to identify sales trends, product performance, customer behavior, city-level performance, and profitability patterns.

The goal is to transform raw sales data into meaningful business insights using Python and data analysis techniques.

---

## Business Questions

The analysis focuses on answering the following questions:

* How does sales performance change over time?
* Which cities generate the highest sales?
* Which products generate the highest sales?
* Which products generate the highest total profit?
* Which products have the highest profit margins?
* Who are the top customers by sales?
* How does Average Order Value vary across cities?
* How does profit margin vary across different discount levels?
* How does product mix differ across cities?
* How does product profitability vary across cities?

---

## Dataset

The dataset contains sales transaction records with the following columns:

| Column     | Description             |
| ---------- | ----------------------- |
| `OrderID`  | Unique order identifier |
| `Date`     | Order date              |
| `Customer` | Customer identifier     |
| `City`     | Customer/order city     |
| `Product`  | Product name            |
| `Category` | Product category        |
| `Quantity` | Quantity ordered        |
| `Sales`    | Sales revenue           |
| `Cost`     | Product cost            |
| `Discount` | Discount percentage     |

The dataset contains **190 transaction records** covering a six-month period.

---

## Data Cleaning

The following data-quality checks were performed:

* Checked the first rows and dataset structure
* Reviewed descriptive statistics
* Checked data types
* Checked missing values
* Checked duplicate records
* Converted the `Date` column to datetime format
* Checked for invalid or non-positive values in:

  * Quantity
  * Sales
  * Cost
* Checked discount values for invalid ranges

No duplicate records or invalid numeric values were identified in the dataset.

---

## Feature Engineering

Several calculated metrics were created to support the analysis.

### Profit

```text
Profit = Sales - Cost
```

### Profit Margin

```text
Profit Margin = (Profit / Sales) × 100
```

### Average Order Value

```text
Average Order Value = Sales / Number of Orders
```

### Month

The month was extracted from the order date to analyze monthly sales performance.

---

## Analysis

### Sales Analysis

Sales were analyzed across:

* Months
* Cities
* Products
* Product categories
* City-product combinations

### Customer Analysis

Customer-level metrics include:

* Total Sales
* Total Profit
* Total Orders
* Average Order Value

Customers were also ranked based on total sales to identify the top 10 customers.

### Product Profitability

Product performance was evaluated using:

* Total Sales
* Total Cost
* Total Profit
* Profit Margin

This helps distinguish between products that generate high total profit and products that have high profit margins.

### Discount Analysis

Different discount levels were compared using:

* Total Sales
* Total Profit
* Number of Orders
* Profit Margin

### City-Product Analysis

Product performance was also analyzed by city using:

* Sales by city and product
* Order count by city and product
* Product mix by city
* Profitability by city and product

---

## Key Findings

### 1. Monthly Sales Variation

Sales varied considerably across the six analyzed months.

* March recorded the highest total sales at approximately **838.9M**.
* May recorded the lowest total sales at approximately **172.5M**.

The results indicate noticeable month-to-month variation in sales performance.

### 2. City Performance

Isfahan generated the highest total sales at approximately **802.9M**.

Karaj recorded the lowest total sales at approximately **130.6M**.

However, total sales and Average Order Value show different patterns. Shiraz recorded the highest Average Order Value at approximately **44.95M**.

### 3. Product Performance

Laptop generated the highest total sales at approximately **1,974M** and the highest total profit at approximately **329M**.

However, Laptop had a profit margin of approximately **16.67%**.

Mouse had the highest profit margin at approximately **41.18%**, despite having much lower total sales.

This demonstrates the difference between total profit and profit margin.

### 4. Customer Behavior

Customer performance varied considerably.

For example:

* Customer_24 generated approximately **111.25M Average Order Value** from only 2 orders.
* Customer_15 had 8 orders but an Average Order Value of approximately **22.88M**.

Therefore, a higher number of orders does not necessarily correspond to a higher Average Order Value.

### 5. Discount Analysis

Profit margins varied across discount levels:

| Discount | Profit Margin |
| -------: | ------------: |
|       0% |        19.65% |
|       5% |        21.07% |
|      10% |        18.35% |
|      15% |        20.12% |

The results do not show a consistent linear relationship between discount level and profit margin in this dataset.

---

## Visualizations

The project includes a six-chart sales analysis dashboard covering:

1. Monthly Sales Trend
2. Sales by City
3. Sales by Product
4. Total Profit by Product
5. Top 10 Customers by Sales
6. Profit Margin by Discount

The dashboard provides a high-level view of sales performance, profitability, customer contribution, and discount patterns.

---

## Tools & Technologies

* Python
* Pandas
* Matplotlib
* Microsoft Excel
* VS Code

---

## Project Structure

```text
sales-analysis/
│
├── data/
│   └── sales_data.xlsx
│
├── src/
│   └── sales_analysis.py
│
├── outputs/
│   └── charts/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## How to Run

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Navigate to the project directory

```bash
cd sales-analysis
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the analysis

```bash
python src/sales_analysis.py
```

---

## Requirements

The main Python libraries used in this project are:

```text
pandas
matplotlib
openpyxl
```

---

## Limitations

This analysis is based on the available transaction dataset and describes patterns observed within the data.

The analysis does not establish causal relationships between variables. For example, differences in sales or profit margin across discount levels should not be interpreted as evidence that discounts directly caused those changes.

The dataset also covers a limited six-month period, so the findings may not represent longer-term seasonal patterns.

---

## Future Improvements

Potential extensions of this project include:

* Building an interactive Power BI dashboard
* Adding more detailed time-series analysis
* Analyzing customer segmentation
* Investigating product-category performance
* Adding statistical analysis
* Exploring relationships between discount, sales volume, and profitability
* Automating the analysis pipeline

---

## Author

**Zahra Amini**

Data Analyst | Product Designer

This project is part of my data analytics portfolio, demonstrating skills in data cleaning, exploratory analysis, KPI development, business analysis, and data visualization.
