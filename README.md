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
  - In manual mode, the script prompts you to enter folder names for each file extension.
  - In automatic mode, the script categorizes files into predefined categories (images, videos, audio, documents, archives, scripts, others).
- Move Files: The script moves files into the corresponding folders based on the folder map.

Auto Categorization Dictionary
The script uses predefined categories for automatic mode:
- Images: .jpg, .jpeg, .png, .gif, .bmp, .tiff
- Videos: .mp4, .avi, .mkv, .mov, .wmv, .flv
- Audio: .mp3, .wav, .aac, .flac, .ogg, .wma
- Documents: .pdf, .doc, .docx, .xls, .xlsx, .ppt, .pptx, .txt
- Archives: .zip, .rar, .7z, .tar, .gz
- Scripts: .py, .js, .html, .css, .sh, .bat
- Others: Any other file extensions not falling into the above categories.

Contributions are welcome! Please feel free to submit a Pull Request or open an issue to discuss improvements or bug fixes.

include scripts to run at specific intervals of time