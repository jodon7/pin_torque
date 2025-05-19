# This script will clean up data from the 'data' directory and save it to the 'cleaned_data' directory.
import os
import pandas as pd



# Prompt user for the new CSV file name
file_name = input("Enter the name for the new CSV file (without .csv extension): ")
file_path = os.path.join('cleaned_data', f"{file_name}.csv")

# Ensure the cleaned_data directory exists
os.makedirs('cleaned_data', exist_ok=True)

# Create an empty DataFrame and save it as a new CSV file
df = pd.DataFrame()
df.to_csv(file_path, index=False)
print(f"Created new CSV file at: {file_path}")
#testing 