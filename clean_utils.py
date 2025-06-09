import csv
import os
import glob

def extract_rows(input_file, writer, header_written):
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = list(csv.reader(infile))
        if not reader or len(reader[0]) < 2:
            return  # Skip files without enough columns
        lot_value = reader[0][1]  # Column 2, row 1
        lot_value_trimmed = lot_value[13:]  # Exclude first 13 characters
        lot_main = lot_value_trimmed[:-6] if len(lot_value_trimmed) > 6 else ''
        lot_parent = lot_value_trimmed[-6:] if len(lot_value_trimmed) >= 6 else lot_value_trimmed
        waferID_value = reader[3][1] if len(reader) > 3 and len(reader[3]) > 1 else ''  # Column 2, row 4
        chamber_value = reader[2][1] if len(reader) > 1 and len(reader[1]) > 1 else ''  # Column 2, row 2

        start_writing = False
        for idx, row in enumerate(reader):
            if len(row) >= 3:
                # Write header only once, with "Lot", "Parent", "waferID", and "chamber" columns
                if row[0] == "Interval" and row[1] == "Section No." and row[2] == "Pin Torque":
                    if not header_written[0]:
                        writer.writerow(row + ["Lot", "Parent", "WaferID", "Chamber"])
                        header_written[0] = True
                    start_writing = True
                    continue  # Skip writing this row again
                # Skip unwanted rows
                if row[0].strip() == "sec" and row[2].strip() == "mV" and row[3].strip() == "mV":
                    continue
            if start_writing:
                writer.writerow(row + [lot_main, lot_parent, waferID_value, chamber_value])

def process_folder(input_folder, output_file):
    csv_files = glob.glob(os.path.join(input_folder, '*.csv'))
    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        header_written = [False]
        for csv_file in csv_files:
            extract_rows(csv_file, writer, header_written)