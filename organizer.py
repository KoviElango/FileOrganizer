import shutil
import os

# Prompt the user for the source directory
source_dir = input("Enter the path for the directory to be organised: ")
base_dir = source_dir + "\\"

# Ask the user for the folder naming option
naming_option = input("Would you like to name the folders manually or automatically? (Enter 'manual' or 'auto'): ").strip().lower()

extensions = set()

for files in os.scandir(source_dir):
    if files.is_file():
        _, suffix = os.path.splitext(files.name)
        extensions.add(suffix)

folder_map = {}

if naming_option == 'manual':
    for ext in extensions:
        folder_name = input(f"Please enter folder name for {ext} files: ")
        folder_path = os.path.join(base_dir, folder_name)
        if folder_name not in folder_map.values():
            os.makedirs(folder_path, exist_ok=True)
        folder_map[ext] = folder_path
        print(f"Mapped {ext} files to folder {folder_name}")
else:
    for ext in extensions:
        folder_name = ext.strip('.').lower() + "_files"
        folder_path = os.path.join(base_dir, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        folder_map[ext] = folder_path
        print(f"Automatically mapped {ext} files to folder {folder_name}")

print("Folders have been created successfully.")

for filename in os.listdir(source_dir):
    file_path = os.path.join(source_dir, filename)
    if os.path.isfile(file_path):
        _, suffix = os.path.splitext(filename)
        if suffix in folder_map:
            destination_dir = folder_map[suffix]
        else:
            destination_dir = os.path.join(base_dir, 'Others')
            os.makedirs(destination_dir, exist_ok=True)
        shutil.move(file_path, destination_dir)
        print(f"Moved {filename} to {destination_dir}")

print("Files have been moved successfully.")
