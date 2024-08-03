File Organizer

The File Organizer Script is a Python program designed to help you organize files in a specified directory by their extensions. We know how our desktop and downloads folder is cluttered. Well, this will help better organise those files. It provides two modes for organizing files: manual and automatic. In manual mode, you can specify the folder names for each file extension. In automatic mode, the script generates folder names based on the file extensions.

Prerequisites

- Python 3.x
- shutil and os modules (these are part of the Python standard library)

Script Workflow
- Input Source Directory: The script prompts you to enter the path of the directory you want to organize.
- Choose Naming Option: The script asks if you want to name the folders manually or automatically.
- Collect Extensions: The script scans the source directory and collects all unique file extensions.
- Create Folder Map
- Move Files: The script moves files into the corresponding folders based on the folder map.

Contributions are welcome! Please feel free to submit a Pull Request or open an issue to discuss improvements or bug fixes.
