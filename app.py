import os

def rename_files():
    directory = input("Please enter the directory path: ")
    rename_all = input("Do you want to rename files in subdirectories as well? Type 'RENAME-ALL-FILES' to confirm: ")
    if rename_all == 'RENAME-ALL-FILES':
        for dirpath, dirnames, filenames in os.walk(directory):
            rename_in_directory(dirpath, filenames)
    else:
        filenames = os.listdir(directory)
        rename_in_directory(directory, filenames)

def rename_in_directory(directory, filenames):
    for filename in filenames:
        if ' ' not in filename and '_' not in filename:
            print(f"Skipped filename: {filename}")
            continue  # Skip files without spaces or underscores
        new_filename = filename.replace(' ', '-').replace('_', '-')
        if new_filename in filenames:
            base, extension = os.path.splitext(new_filename)
            i = 1
            while new_filename in filenames:
                new_filename = f"{base}-copy{i}{extension}"
                i += 1
            print(f"Filename conflict: {base + extension} already exists. Renaming conflicted file to {new_filename}")
        else:
            print(f"Renamed {filename} to {new_filename}")
        source = os.path.join(directory, filename)
        destination = os.path.join(directory, new_filename)
        os.rename(source, destination)  # Rename the file

# Usage
rename_files()