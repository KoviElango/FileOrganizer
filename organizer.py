import shutil
import os

def get_source_directory():
    try:
        source_dir = input("Enter the path for the directory to be organised: ")
        source_dir = os.path.normpath(source_dir)
        if not os.path.exists(source_dir):
            raise FileNotFoundError(f"The directory {source_dir} does not exist.")
        return source_dir
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

def get_naming_option():
    try:
        naming_option = input("Would you like to name the folders manually or automatically? (Enter 'manual' or 'auto'): ").strip().lower()
        if naming_option not in ['manual', 'auto']:
            raise ValueError("Invalid input. Please enter 'manual' or 'auto'.")
        return naming_option
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

def collect_extensions(source_dir):
    try:
        extensions = set()
        for files in os.scandir(source_dir):
            if files.is_file():
                _, suffix = os.path.splitext(files.name)
                extensions.add(suffix)
        return extensions
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

def create_folder_map(extensions, base_dir, naming_option):
    folder_map = {}
    
    auto_categories = {
        'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
        'videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv'],
        'audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.wma'],
        'documents': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt'],
        'archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'scripts': ['.py', '.js', '.html', '.css', '.sh', '.bat'],
        'others': []
    }
    
    try:
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
                categorized = False
                for category, ext_list in auto_categories.items():
                    if ext in ext_list:
                        folder_name = category.capitalize() + "_files"
                        folder_path = os.path.join(base_dir, folder_name)
                        os.makedirs(folder_path, exist_ok=True)
                        folder_map[ext] = folder_path
                        print(f"Automatically mapped {ext} files to folder {folder_name}")
                        categorized = True
                        break
                if not categorized:
                    auto_categories['others'].append(ext)
                    folder_name = "Others_files"
                    folder_path = os.path.join(base_dir, folder_name)
                    os.makedirs(folder_path, exist_ok=True)
                    folder_map[ext] = folder_path
                    print(f"Automatically mapped {ext} files to folder {folder_name}")
        return folder_map
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

def move_files(source_dir, base_dir, folder_map):
    try:
        for filename in os.listdir(source_dir):
            file_path = os.path.join(source_dir, filename)
            if os.path.isfile(file_path):
                _, suffix = os.path.splitext(filename)
                if suffix in folder_map:
                    destination_dir = folder_map[suffix]
                else:
                    destination_dir = os.path.join(base_dir, 'Others_files')
                    os.makedirs(destination_dir, exist_ok=True)
                shutil.move(file_path, destination_dir)
                print(f"Moved {filename} to {destination_dir}")
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

def main():
    try:
        source_dir = get_source_directory()
        base_dir = source_dir
        naming_option = get_naming_option()
        extensions = collect_extensions(source_dir)
        folder_map = create_folder_map(extensions, base_dir, naming_option)
        print("Folders have been created successfully.")
        move_files(source_dir, base_dir, folder_map)
        print("Files have been moved successfully.")
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()
