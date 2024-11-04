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

# Save the result to a CSV file
most_sold_products_file = "most_sold_products.csv"
most_sold_products.to_csv(most_sold_products_file, index=False)

# Print success message
print(f"Most sold products saved to {most_sold_products_file}.")
