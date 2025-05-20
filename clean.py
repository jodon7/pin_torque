import csv

def extract_rows(input_file, output_file):
    # Open the input CSV file for reading
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        
        # Open the output CSV file for writing
        with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            
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

# Example usage
input_csv = 'test.csv'  # Replace with your input CSV file path
output_csv = 'output.csv'  # Replace with your desired output CSV file path

extract_rows(input_csv, output_csv)