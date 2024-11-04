from pymongo import MongoClient
import pandas as pd

# MongoDB connection setup
client = MongoClient("mongodb+srv://donachinthapasan01:EoxpE2X83sE4Du1q@nextAuthDB.25ujz.mongodb.net/nextAuthDB?retryWrites=true&w=majority")
db = client["csv_analysis"]
collection = db["csv"]

# Retrieve data from MongoDB
data = pd.DataFrame(list(collection.find()))

# Clean column names (replace spaces with underscores)
data.columns = data.columns.str.replace(' ', '_')

# 3. Find the most profitable product category
# Use Total_Price to determine profitability
most_profitable_category = data.groupby('Category')['Total_Price'].sum().reset_index()
most_profitable_category = most_profitable_category.sort_values(by='Total_Price', ascending=False)

# Save the result to a CSV file
most_profitable_category_file = "most_profitable_category.csv"
most_profitable_category.to_csv(most_profitable_category_file, index=False)

# Print success message
print(f"Most profitable category saved to {most_profitable_category_file}.")
