import shutil
import os
import logging
from collections import defaultdict

logging.basicConfig(filename='file_organizer.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_and_print(message):
    print(message)
    logging.info(message)

def get_source_directory():
    source_dir = input("Enter the path for the directory to be organised: ")
    source_dir = os.path.normpath(source_dir)
    if not os.path.exists(source_dir):
        log_and_print(f"Error: The directory {source_dir} does not exist.")
        exit(1)
    return source_dir

def get_naming_option():
    naming_option = input("Would you like to name the folders manually or automatically? (Enter 'manual' or 'auto'): ").strip().lower()
    if naming_option not in ['manual', 'auto']:
        log_and_print("Error: Invalid input. Please enter 'manual' or 'auto'.")
        exit(1)
    return naming_option

def collect_extensions(source_dir):
    extensions = set()
    for files in os.scandir(source_dir):
        if files.is_file():
            _, suffix = os.path.splitext(files.name)
            extensions.add(suffix)
    return extensions

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
    
    if naming_option == 'manual':
        for ext in extensions:
            folder_name = input(f"Please enter folder name for {ext} files: ")
            folder_path = os.path.join(base_dir, folder_name)
            if folder_name not in folder_map.values():
                try:
                    os.makedirs(folder_path, exist_ok=True)
                except Exception as e:
                    log_and_print(f"Error creating directory {folder_path}: {e}")
                    exit(1)
            folder_map[ext] = folder_path
            log_and_print(f"Mapped {ext} files to folder {folder_name}")
            log_and_print("Current folder mappings:")
            for k, v in folder_map.items():
                log_and_print(f"Extension: {k} -> Folder: {v}")
    else:
        for ext in extensions:
            categorized = False
            for category, ext_list in auto_categories.items():
                if ext in ext_list:
                    folder_name = category.capitalize() + "_files"
                    folder_path = os.path.join(base_dir, folder_name)
                    try:
                        os.makedirs(folder_path, exist_ok=True)
                    except Exception as e:
                        log_and_print(f"Error creating directory {folder_path}: {e}")
                        exit(1)
                    folder_map[ext] = folder_path
                    log_and_print(f"Automatically mapped {ext} files to folder {folder_name}")
                    categorized = True
                    break
            if not categorized:
                auto_categories['others'].append(ext)
                folder_name = "Others_files"
                folder_path = os.path.join(base_dir, folder_name)
                try:
                    os.makedirs(folder_path, exist_ok=True)
                except Exception as e:
                    log_and_print(f"Error creating directory {folder_path}: {e}")
                    exit(1)
                folder_map[ext] = folder_path
                log_and_print(f"Automatically mapped {ext} files to folder {folder_name}")
    return folder_map

def move_files(source_dir, base_dir, folder_map, dry_run=False):
    report_dict = defaultdict(list)
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        if os.path.isfile(file_path):
            _, suffix = os.path.splitext(filename)
            if suffix in folder_map:
                destination_dir = folder_map[suffix]
            else:
                destination_dir = os.path.join(base_dir, 'Others_files')
                try:
                    os.makedirs(destination_dir, exist_ok=True)
                except Exception as e:
                    log_and_print(f"Error creating directory {destination_dir}: {e}")
                    exit(1)
            if dry_run:
                log_and_print(f"[DRY RUN] Would move {filename} to {destination_dir}")
                report_dict[destination_dir].append(f"[DRY RUN] Would move {filename}")
            else:
                try:
                    shutil.move(file_path, destination_dir)
                    log_and_print(f"Moved {filename} to {destination_dir}")
                    report_dict[destination_dir].append(f"Moved {filename}")
                except Exception as e:
                    log_and_print(f"Error moving file {filename} to {destination_dir}: {e}")
                    exit(1)
    return report_dict

def write_report(report_dict, source_dir):
    report_path = os.path.join(source_dir, "file_organizer_report.txt")
    try:
        with open(report_path, 'w') as report_file:
            for folder, files in report_dict.items():
                report_file.write(f"Folder: {folder}\n")
                for file in files:
                    report_file.write(f"    {file}\n")
                report_file.write("\n")
        log_and_print(f"Report written to {report_path}")
    except Exception as e:
        log_and_print(f"Error writing report to {report_path}: {e}")
        exit(1)

def perform_dry_run(source_dir, base_dir, folder_map):
    log_and_print("Performing dry run...")
    report_dict = move_files(source_dir, base_dir, folder_map, dry_run=True)
    write_report(report_dict, source_dir)
    log_and_print("Dry run completed. No files were moved.")
    return report_dict

def main():
    source_dir = get_source_directory()
    base_dir = source_dir
    naming_option = get_naming_option()
    dry_run_option = input("Would you like to perform a dry run? (Enter 'yes' or 'no'): ").strip().lower()
    dry_run = dry_run_option == 'yes'
    extensions = collect_extensions(source_dir)
    folder_map = create_folder_map(extensions, base_dir, naming_option)
    log_and_print("Folders have been created successfully.")

    if dry_run:
        report_dict = perform_dry_run(source_dir, base_dir, folder_map)
        proceed_option = input("Would you like to proceed with moving the files? (Enter 'yes' or 'no'): ").strip().lower()
        if proceed_option == 'yes':
            report_dict = move_files(source_dir, base_dir, folder_map, dry_run=False)
            write_report(report_dict, source_dir)
            log_and_print("Files have been moved successfully.")
        else:
            log_and_print("Operation cancelled. No files were moved.")
    else:
        report_dict = move_files(source_dir, base_dir, folder_map, dry_run=False)
        write_report(report_dict, source_dir)
        log_and_print("Files have been moved successfully.")

if __name__ == "__main__":
    main()
