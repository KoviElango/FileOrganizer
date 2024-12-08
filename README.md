from docx import Document

# Create a new Document
doc = Document()

# Add Title
doc.add_heading('File Organizer', level=1)

# Add Description
doc.add_paragraph(
    "The **File Organizer Script** is a Python program that organizes files in a specified directory by their extensions. "
    "It helps declutter messy folders like Desktop or Downloads by categorizing files into folders. "
    "The script supports **Manual** and **Automatic** modes for organizing files:"
)
doc.add_paragraph(
    "- **Manual Mode**: Lets you specify folder names for each file extension.\n"
    "- **Automatic Mode**: Automatically generates folder names based on predefined categories."
)

# Add Prerequisites Section
doc.add_heading('Prerequisites', level=2)
doc.add_paragraph("- Python 3.x")
doc.add_paragraph("- `shutil` and `os` (part of the Python standard library)")

# Add Workflow Section
doc.add_heading('Workflow', level=2)
doc.add_paragraph(
    "1. **Input Source Directory**: Enter the directory path to organize.\n"
    "2. **Choose Mode**: Specify folder names manually or use predefined automatic categorization.\n"
    "3. **Collect Extensions**: Scan the directory to identify unique file extensions.\n"
    "4. **Create Folder Map**:\n"
    "   - **Manual Mode**: Enter folder names for each file extension.\n"
    "   - **Automatic Mode**: Categorize files using predefined categories.\n"
    "5. **Move Files**: Organize files into the mapped folders."
)

# Add Auto Categorization Dictionary Section
doc.add_heading('Auto Categorization Dictionary', level=2)
doc.add_paragraph(
    "The script uses these categories in automatic mode:\n"
    "- **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`\n"
    "- **Videos**: `.mp4`, `.avi`, `.mkv`, `.mov`, `.wmv`, `.flv`\n"
    "- **Audio**: `.mp3`, `.wav`, `.aac`, `.flac`, `.ogg`, `.wma`\n"
    "- **Documents**: `.pdf`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.ppt`, `.pptx`, `.txt`\n"
    "- **Archives**: `.zip`, `.rar`, `.7z`, `.tar`, `.gz`\n"
    "- **Scripts**: `.py`, `.js`, `.html`, `.css`, `.sh`, `.bat`\n"
    "- **Others**: Extensions not listed above."
)

# Add Contributions Section
doc.add_heading('Contributions', level=2)
doc.add_paragraph(
    "Contributions are welcome! Submit a Pull Request or open an issue to suggest improvements."
)

# Add Future Scope Section
doc.add_heading('Future Scope', level=2)
doc.add_heading('Suggested Improvements:', level=3)
doc.add_paragraph(
    "- **Scheduler Integration**: Enable periodic execution to keep directories automatically organized.\n"
    "- **GUI Interface**: Add a user-friendly graphical interface for easier configuration.\n"
    "- **Cloud Integration**: Support for organizing files in cloud directories (e.g., Google Drive, Dropbox).\n"
    "- **Customization Options**: Allow users to define their own categories and rules.\n"
    "- **Multi-Language Support**: Add translations for a global user base.\n"
    "- **File Preview Feature**: Provide a preview of how files will be organized before execution."
)

# Save the Document
file_path = "/mnt/data/File_Organizer_Documentation.docx"
doc.save(file_path)

file_path
