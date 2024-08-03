import shutil
import os

source_dir = input("Enter the path for the directory to be organised:")
base_dir = source_dir + "\\"

extensions = set()

for files in os.scandir(source_dir):
    if files.is_file():
        _, suffix = os.path.splitext(files.name)
        extensions.add(suffix)

folder_map = {}

for ext in extensions:
    folder_name = input(f"Please enter folder name for {ext} files: ")
    folder_path = os.path.join(base_dir, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    folder_map[ext] = folder_path
    print(f"Created folder {folder_name} for {ext} files.")

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