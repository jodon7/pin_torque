import csv
import os
import glob

def extract_rows(input_file, writer, header_written):
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        start_writing = False

        for row in reader:
            if len(row) >= 3:
                # Write header only once
                if row[0] == "Interval" and row[1] == "Section No." and row[2] == "Pin Torque":
                    if not header_written[0]:
                        writer.writerow(row)
                        header_written[0] = True
                    start_writing = True
                    continue  # Skip writing this row again
                # Skip unwanted rows
                if row[0].strip() == "sec" and row[2].strip() == "mV" and row[3].strip() == "mV":
                    continue
            if start_writing:
                writer.writerow(row)

def process_folder(input_folder, output_file):
    csv_files = glob.glob(os.path.join(input_folder, '*.csv'))
    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        header_written = [False]
        for csv_file in csv_files:
            extract_rows(csv_file, writer, header_written)

input_folder = 'data'  # Replace with your folder path containing CSV files
output_csv = 'output.csv'  # Replace with your desired output CSV file path

process_folder(input_folder, output_csv)