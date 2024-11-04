from pymongo import MongoClient
import pandas as pd

# MongoDB connection setup
client = MongoClient("mongodb+srv://donachinthapasan01:EoxpE2X83sE4Du1q@nextAuthDB.25ujz.mongodb.net/nextAuthDB?retryWrites=true&w=majority")
db = client["csv_analysis"]
collection = db["csv"]

# Retrieve data from MongoDB
data = pd.DataFrame(list(collection.find()))

# Check if the expected columns exist
if 'Category' in data.columns and 'Product' in data.columns:
    # Filter the DataFrame to keep only 'Category' and 'Product'
    filtered_data = data[['Category', 'Product']]

    # Group by Category and aggregate products
    grouped_data = filtered_data.groupby('Category')['Product'].apply(list).reset_index()

    # Save the grouped data to a new CSV file
    output_file_path = "categories_and_products.csv"
    grouped_data.to_csv(output_file_path, index=False)

    print(f"Categories and their respective products saved to {output_file_path}.")
else:
    print("Required columns 'Category' or 'Product' not found in the data.")
