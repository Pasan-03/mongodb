from pymongo import MongoClient
import pandas as pd

# MongoDB connection setup
client = MongoClient("mongodb+srv://donachinthapasan01:EoxpE2X83sE4Du1q@nextAuthDB.25ujz.mongodb.net/nextAuthDB?retryWrites=true&w=majority")
db = client["csv_analysis"]
collection = db["csv"]

# Retrieve data from MongoDB
data = pd.DataFrame(list(collection.find()))

# 1. Find which products are sold the most
most_sold_products = data.groupby('Product')['Quantity'].sum().reset_index()
most_sold_products = most_sold_products.sort_values(by='Quantity', ascending=False)
most_sold_products_file = "most_sold_products.csv"
most_sold_products.to_csv(most_sold_products_file, index=False)

# 2. Find the most used payment method
most_used_payment_method = data['Payment_Method'].value_counts().reset_index()
most_used_payment_method.columns = ['Payment_Method', 'Count']
most_used_payment_method_file = "most_used_payment_method.csv"
most_used_payment_method.to_csv(most_used_payment_method_file, index=False)

# 3. Find the most profitable product category
# Calculate profit per product (assuming Profit = Price * Quantity)
data['Total Profit'] = data['Price_per_Unit'] * data['Quantity']
most_profitable_category = data.groupby('Category')['Total Profit'].sum().reset_index()
most_profitable_category = most_profitable_category.sort_values(by='Total Profit', ascending=False)
most_profitable_category_file = "most_profitable_category.csv"
most_profitable_category.to_csv(most_profitable_category_file, index=False)

# Print success messages
print(f"Most sold products saved to {most_sold_products_file}.")
print(f"Most used payment method saved to {most_used_payment_method_file}.")
print(f"Most profitable category saved to {most_profitable_category_file}.")
