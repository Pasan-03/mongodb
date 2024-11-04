from pymongo import MongoClient
import pandas as pd

# MongoDB connection setup
client = MongoClient("mongodb+srv://donachinthapasan01:EoxpE2X83sE4Du1q@nextAuthDB.25ujz.mongodb.net/nextAuthDB?retryWrites=true&w=majority")
db = client["csv_analysis"]  # Creating a new database named 'csv_analysis'
collection = db["csv"]  # Creating a new collection named 'csv'

# Load the CSV file
csv_file_path = "e_commerce_data.csv"  # CSV file in the same directory
data = pd.read_csv(csv_file_path)  # Read the CSV file

# Convert CSV data to dictionary format
data_dict = data.to_dict("records")

# Insert data into MongoDB collection
collection.insert_many(data_dict)
print("Data inserted successfully into csv_analysis.csv.")
