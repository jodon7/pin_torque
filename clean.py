import csv
import os
import glob

def extract_rows(input_file, writer):
    # Open the input CSV file for reading
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        
        # Flag to start writing rows to the new CSV
        start_writing = False
        
        for row in reader:
            # Print the row for debugging purposes
            print(f"Processing row: {row}")
            
            # Check if the row has at least 3 columns
            if len(row) >= 3:
                # Check if the current row matches the specified criteria
                if row[0] == "Interval" and row[1] == "Section No." and row[2] == "Pin Torque":
                    start_writing = True
                    print("Found the target row. Starting to write subsequent rows.")
            
            # If the flag is set, write the row to the output file
            if start_writing:
                writer.writerow(row)

def process_folder(input_folder, output_file):
    # Get a list of all CSV files in the input folder
    csv_files = glob.glob(os.path.join(input_folder, '*.csv'))
    
    # Open the output CSV file for writing
    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        
        # Process each CSV file in the folder
        for csv_file in csv_files:
            print(f"Processing file: {csv_file}")
            extract_rows(csv_file, writer)

# Example usage
input_folder = 'data'  # Replace with your folder path containing CSV files
output_csv = 'output.csv'  # Replace with your desired output CSV file path

process_folder(input_folder, output_csv)