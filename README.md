File Organizer

The File Organizer Script is a Python program that organizes files in a specified directory by their extensions. It helps declutter messy folders like Desktop or Downloads by categorizing files into folders. The script supports Manual and Automatic modes for organizing files:
	•	Manual Mode: Lets you specify folder names for each file extension.
	•	Automatic Mode: Automatically generates folder names based on predefined categories.

Prerequisites

	•	Python 3.x
	•	shutil and os (part of the Python standard library)

Workflow

	1.	Input Source Directory: Enter the directory path to organize.
	2.	Choose Mode: Specify folder names manually or use predefined automatic categorization.
	3.	Collect Extensions: Scan the directory to identify unique file extensions.
	4.	Create Folder Map:
	•	Manual Mode: Enter folder names for each file extension.
	•	Automatic Mode: Categorize files using predefined categories.
	5.	Move Files: Organize files into the mapped folders.

Auto Categorization Dictionary

The script uses these categories in automatic mode:
	•	Images: .jpg, .jpeg, .png, .gif, .bmp, .tiff
	•	Videos: .mp4, .avi, .mkv, .mov, .wmv, .flv
	•	Audio: .mp3, .wav, .aac, .flac, .ogg, .wma
	•	Documents: .pdf, .doc, .docx, .xls, .xlsx, .ppt, .pptx, .txt
	•	Archives: .zip, .rar, .7z, .tar, .gz
	•	Scripts: .py, .js, .html, .css, .sh, .bat
	•	Others: Extensions not listed above.

Contributions

Contributions are welcome! Submit a Pull Request or open an issue to suggest improvements.

Future Scope

Suggested Improvements:

	•	Scheduler Integration: Enable periodic execution to keep directories automatically organized.
	•	GUI Interface: Add a user-friendly graphical interface for easier configuration.
	•	Cloud Integration: Support for organizing files in cloud directories (e.g., Google Drive, Dropbox).
	•	Customization Options: Allow users to define their own categories and rules.
	•	Multi-Language Support: Add translations for a global user base.
	•	File Preview Feature: Provide a preview of how files will be organized before execution.
