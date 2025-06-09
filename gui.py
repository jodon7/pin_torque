import tkinter as tk
from tkinter import filedialog, messagebox
from clean_utils import process_folder  # Import your functions

def run_processing(input_folder, output_file):
    try:
        process_folder(input_folder, output_file)
        messagebox.showinfo("Success", f"Processing complete!\nOutput saved to:\n{output_file}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def select_input_folder():
    folder = filedialog.askdirectory()
    if folder:
        input_folder_var.set(folder)

def select_output_file():
    file = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if file:
        output_file_var.set(file)

def on_run():
    input_folder = input_folder_var.get()
    output_file = output_file_var.get()
    if not input_folder or not output_file:
        messagebox.showwarning("Missing Info", "Please select both input folder and output file.")
        return
    run_processing(input_folder, output_file)

# Tkinter GUI
root = tk.Tk()
root.title("CSV Pin Torque Cleaner")

input_folder_var = tk.StringVar()
output_file_var = tk.StringVar()

tk.Label(root, text="Input Folder:").grid(row=0, column=0, sticky="e")
tk.Entry(root, textvariable=input_folder_var, width=40).grid(row=0, column=1)
tk.Button(root, text="Browse...", command=select_input_folder).grid(row=0, column=2)

tk.Label(root, text="Output File:").grid(row=1, column=0, sticky="e")
tk.Entry(root, textvariable=output_file_var, width=40).grid(row=1, column=1)
tk.Button(root, text="Browse...", command=select_output_file).grid(row=1, column=2)

tk.Button(root, text="Run", command=on_run, width=20).grid(row=2, column=0, columnspan=3, pady=10)

# Add note for support email
tk.Label(
    root,
    text="For questions, email john.odonovan@intel.com",
    fg="blue"
).grid(row=3, column=0, columnspan=3, pady=(10, 0))

root.mainloop()