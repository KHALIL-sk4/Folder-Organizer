import os
import shutil

destination_folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mov"],
    "Music": [".mp3", ".wav"],
    "Applications": [".exe"],
    "Zip": [".rar",".zip",".cab",".arj",".lzh",".tar",".gzip",".uue",".iso",".bzip2",".7z"]
}

def organize_files(source_folder):
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        if os.path.isdir(file_path):
            continue
        _, file_extension = os.path.splitext(filename)
        for category, extensions in destination_folders.items():
            if file_extension.lower() in extensions:
                category_folder = os.path.join(source_folder, category)
                os.makedirs(category_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(category_folder, filename))
                print(f"Moved {filename} to {category}")
                break

source_folder = input("Enter the path of the folder you want to organize: ")
organize_files(source_folder)
