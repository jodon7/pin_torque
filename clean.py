# This script will clean up data from the 'data' directory and save it to the 'cleaned_data' directory.
import os
import pandas as pd



# Prompt user for the new CSV file name
file_name = input("Enter the name for the new CSV file (without .csv extension): ")
file_path = os.path.join('cleaned_data', f"{file_name}.csv")
# Define the column headers for the new CSV file
column_headers = ["Interval", "Section No.", "Pin Torque", "Pin Speed"]
# Ensure the cleaned_data directory exists
os.makedirs('cleaned_data', exist_ok=True)

csv_files = [f for f in os.listdir('data') if f.endswith('.csv') and f != f"{file_name}.csv"]
dfs = []

for csv_file in csv_files:
    csv_path = os.path.join('data', csv_file)
    df = pd.read_csv(csv_path, header=None)
    # Find the header row
    header_row = None
    for idx, row in df.iterrows():
        if (
            str(row[0]).strip() == "Interval"
            and str(row[1]).strip() == "Section No."
            and str(row[2]).strip() == "Pin Torque"
            and str(row[3]).strip() == "Pin Speed"
        ):
            header_row = idx
            break
    if header_row is not None:
        df = pd.read_csv(csv_path, header=header_row)
        dfs.append(df)

if dfs:
    combined_df = pd.concat(dfs, ignore_index=True)
    combined_df.to_csv(file_path, index=False)
else:
    print("No files matched the required header conditions.")
