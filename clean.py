# This script will clean up data from the 'data' directory and save it to the 'cleaned_data' directory.
import os
import pandas as pd

new_csv_name = input("Enter the name for the new cleaned CSV file (without extension): ")
new_csv_name = new_csv_name.strip() + ".csv"
cleaned_data_dir = "cleaned_data"
os.makedirs(cleaned_data_dir, exist_ok=True)
column_headers = ["Interval", "Section No.", "Pin Torque", "Pin Speed"]
df = pd.DataFrame(columns=column_headers)
df.to_csv(os.path.join(cleaned_data_dir, new_csv_name), index=False)

# Read all CSV files from the 'data' directory
data_dir = "data"
for filename in os.listdir(data_dir):
    if filename.endswith(".csv"):
        file_path = os.path.join(data_dir, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                row = [cell.strip() for cell in line.strip().split(",")]
                # Check if the first four columns match the pattern
                if len(row) >= 4 and row[0] == "Interval" and row[1] == "Section No." and row[2] == "Pin Torque" and row[3] == "Pin Speed":
                    # All values after the pattern (columns 5+)
                    new_row = row[4:]
                    if new_row:
                        # Pad to match the number of columns if needed
                        while len(new_row) < len(column_headers):
                            new_row.append("")
                        df.loc[len(df)] = new_row[:len(column_headers)]
# Save the combined cleaned data
df.to_csv(os.path.join(cleaned_data_dir, new_csv_name), index=False)
