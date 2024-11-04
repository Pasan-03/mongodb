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

# 2. Find the most used payment method
most_used_payment_method = data['Payment_Method'].value_counts().reset_index()
most_used_payment_method.columns = ['Payment Method', 'Count']

# Save the result to a CSV file
most_used_payment_method_file = "most_used_payment_method.csv"
most_used_payment_method.to_csv(most_used_payment_method_file, index=False)

# Print success message
print(f"Most used payment method saved to {most_used_payment_method_file}.")
