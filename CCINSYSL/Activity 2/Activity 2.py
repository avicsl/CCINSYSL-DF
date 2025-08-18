# clean_data.py

import pandas as pd
import os
import sys

# Define file paths
raw_data_path = 'raw_evidence.csv'
cleaned_data_path = 'cleaned_evidence.csv'

# Check if raw data file exists
if not os.path.exists(raw_data_path):
    print(f"Error: '{raw_data_path}' not found. Please complete Week 1 activity first.")
    sys.exit(1)

# Load the raw data
df = pd.read_csv(raw_data_path)

# Handle missing values
df.fillna('UNKNOWN', inplace=True)

# Convert timestamp column to datetime objects
try:
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
except Exception as e:
    print(f"Error parsing timestamps: {e}")
    sys.exit(1)

# Optional: Drop rows where timestamp could not be parsed (if any)
df = df[df['timestamp'].notnull()]

# Save the cleaned data to a new CSV file
df.to_csv(cleaned_data_path, index=False)

# Output confirmation and preview
print(f"✅ Successfully cleaned and saved data to '{cleaned_data_path}'.")
print("\n📋 First 5 rows of cleaned data:")
print(df.head())
