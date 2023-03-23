import os
import glob
import shutil
import time
import getpass

# mapping each extension with its corresponding folder
# For example, 'jpg', 'png', 'ico', 'gif', 'svg' files will be moved to 'images' folder
# feel free to change based on your needs
extensions = {
    ".jpg": "images",
    ".jpeg": "images",
    ".c": "C Files",
    ".png": "images",
    ".ico": "images",
    ".gif": "images",
    ".svg": "images",
    ".sql": "sql",
    ".exe": "programs",
    ".msi": "programs",
    ".pdf": "pdf",
    ".xlsx": "excel",
    ".csv": "excel",
    ".rar": "archive",
    ".zip": "archive",
    ".gz": "archive",
    ".tar": "archive",
    ".7z": "archive",
    ".docx": "word",
    ".torrent": "torrent",
    ".txt": "text",
    ".ipynb": "python",
    ".py": "python",
    ".pptx": "powerpoint",
    ".ppt": "powerpoint",
    ".mp3": "audio",
    ".wav": "audio",
    ".mp4": "video",
    ".m3u8": "video",
    ".webm": "video",
    ".ts": "typescript",
    ".json": "json",
    ".css": "web",
    ".js": "web",
    ".html": "web",
    ".apk": "apk",
    ".sqlite3": "sqlite3",
}

def organize_downloads_folder():
    print("Organizing Downloads Folder...")
    time.sleep(1)
    
    name = getpass.getuser()
    path = os.path.expanduser(f"~\\Downloads")
    verbose = 1
    
    for extension, folder_name in extensions.items():
        # get all the files matching the extension
        files = glob.glob(os.path.join(path, f"*{extension}"))
        if verbose == 1:
            print(f"[*] Found {len(files)} files with {extension} extension")
        if files:
            # create the folder if it does not exist before
            folder_path = os.path.join(path, folder_name)
            os.makedirs(folder_path, exist_ok=True)
            if verbose == 1:
                print(f"[+] Created {folder_path}")
        for file in files:
            # for each file in that extension, move it to the corresponding folder
            basename = os.path.basename(file)
            dst = os.path.join(path, folder_name, basename)
            if os.path.abspath(file) == os.path.abspath(dst):
                continue  # Skip if source and destination are the same file
            if verbose == 1:
                print(f"[*] Moving {file} to {dst}")
            shutil.move(file, dst)

def add_to_startup():
    file_path = os.path.abspath(__file__)
    bat_path = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
    with open(os.path.join(bat_path, "open.bat"), "w+") as bat_file:
        bat_file.write(f'''@echo off
python "{file_path}"
exit ''')

if __name__ == "__main__":
    organize_downloads_folder()
    add_to_startup()