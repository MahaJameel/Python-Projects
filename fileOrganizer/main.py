import os
import shutil
from pathlib import Path

# Define file category mappings by extension
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".rtf", ".xls", ".xlsx", ".ppt", ".pptx", ".csv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Code": [".py", ".html", ".css", ".js", ".json", ".cpp", ".c", ".java"],
    "Executables": [".exe", ".msi", ".dmg", ".sh"]
}

def organize_folder(target_path: str):
    """
    Organizes files in target_path into category folders based on file extensions.
    """
    target_dir = Path(target_path)

    # Check if the path exists and is a directory
    if not target_dir.exists() or not target_dir.is_dir():
        print(f"Error: The path '{target_path}' is invalid or does not exist.")
        return

    print(f"Organizing files in: {target_dir.resolve()}\n")

    moved_count = 0

    for file in target_dir.iterdir():
        # Ignore subdirectories and system/hidden files
        if file.is_dir() or file.name.startswith('.'):
            continue

        file_extension = file.suffix.lower()
        destination_folder = "Others"  # Default folder for unknown types

        # Identify which category the file belongs to
        for category, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                destination_folder = category
                break

        # Create destination directory if it doesn't exist
        destination_dir = target_dir / destination_folder
        destination_dir.mkdir(exist_ok=True)

        # Move the file
        destination_path = destination_dir / file.name
        
        # Handle file collision (if file with same name already exists)
        if destination_path.exists():
            stem = file.stem
            destination_path = destination_dir / f"{stem}_copy{file.suffix}"

        shutil.move(str(file), str(destination_path))
        print(f"Moved: '{file.name}' -> {destination_folder}/")
        moved_count += 1

    print(f"\nCompleted! Total files organized: {moved_count}")

if __name__ == "__main__":
    # Replace with the folder path you want to organize
    folder_to_organize = r"C:\Users\Maha Jameel\Downloads"
    
    organize_folder(folder_to_organize)