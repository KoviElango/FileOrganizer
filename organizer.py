import shutil
import os

def get_source_directory():
    source_dir = input("Enter the path for the directory to be organised: ")
    source_dir = os.path.normpath(source_dir)
    return source_dir

def get_naming_option():
    return input("Would you like to name the folders manually or automatically? (Enter 'manual' or 'auto'): ").strip().lower()

def collect_extensions(source_dir):
    extensions = set()
    for files in os.scandir(source_dir):
        if files.is_file():
            _, suffix = os.path.splitext(files.name)
            extensions.add(suffix)
    return extensions

def create_folder_map(extensions, base_dir, naming_option):
    folder_map = {}
    if naming_option == 'manual':
        for ext in extensions:
            folder_name = input(f"Please enter folder name for {ext} files: ")
            folder_path = os.path.join(base_dir, folder_name)
            if folder_name not in folder_map.values():
                os.makedirs(folder_path, exist_ok=True)
            folder_map[ext] = folder_path
            print(f"Mapped {ext} files to folder {folder_name}")
            print("Current folder mappings:")
            for k, v in folder_map.items():
                print(f"Extension: {k} -> Folder: {v}")
    else:
        for ext in extensions:
            folder_name = ext.strip('.').lower() + "_files"
            folder_path = os.path.join(base_dir, folder_name)
            os.makedirs(folder_path, exist_ok=True)
            folder_map[ext] = folder_path
            print(f"Automatically mapped {ext} files to folder {folder_name}")
    return folder_map

def move_files(source_dir, base_dir, folder_map):
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

def main():
    source_dir = get_source_directory()
    base_dir = source_dir
    naming_option = get_naming_option()
    extensions = collect_extensions(source_dir)
    folder_map = create_folder_map(extensions, base_dir, naming_option)
    print("Folders have been created successfully.")
    move_files(source_dir, base_dir, folder_map)
    print("Files have been moved successfully.")

if __name__ == "__main__":
    main()
