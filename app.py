import os
import tkinter as tk
from tkinter import filedialog,  messagebox

def rename_files():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    directory = filedialog.askdirectory()
    rename_all = messagebox.askyesno("Rename All Files", "Do you want to rename files in subdirectories as well?")
    if rename_all:
        for dirpath, dirnames, filenames in os.walk(directory):
            rename_in_directory(dirpath, filenames)
    else:
        filenames = os.listdir(directory)
        rename_in_directory(directory, filenames)

def rename_in_directory(directory, filenames):
    for filename in filenames:
        old_file_path = os.path.join(directory, filename)
        if not os.path.isfile(old_file_path):
            continue
        if ' ' not in filename and '_' not in filename:
            print(f"Skipped filename: {filename}")
            continue  # Skip files without spaces or underscores
        new_filename = filename.replace(' ', '-').replace('_', '-')
        new_file_path = os.path.join(directory, new_filename)
        if os.path.exists(new_file_path):
            base, extension = os.path.splitext(new_filename)
            i  = 1
            while os.path.exists(new_file_path):
                new_filename = f"{base}-copy{i}{extension}"
                new_file_path = os.path.join(directory, new_filename)
                i += 1
            print(f"Filename conflict: {base + extension} already exists. Renaming conflicted file to {new_filename}")
        else:
            print(f"Renamed {filename} to {new_filename}")
        os.rename(old_file_path, new_file_path)

# Usage
rename_files()