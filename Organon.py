import os
import glob
import shutil
import time
import getpass

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
    
    username = getpass.getuser()
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    verbose = 1
    
    files = [f for ext in extensions for f in glob.glob(os.path.join(downloads_path, f"*{ext}"))]
    if verbose:
        print(f"[*] Found {len(files)} files to organize")
        
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        folder_name = extensions.get(ext, "others")
        folder_path = os.path.join(downloads_path, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        dst = os.path.join(folder_path, os.path.basename(file))
        if os.path.abspath(file) == os.path.abspath(dst):
            continue
        if verbose:
            print(f"[*] Moving {file} to {dst}")
        shutil.move(file, dst)

def add_to_startup():
    ans = input("Do you want to add the script to the system startup? (y/n): ").lower()
    if ans == "y":
        file_path = os.path.abspath(__file__)
        bat_path = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
        with open(os.path.join(bat_path, "open.bat"), "w+") as bat_file:
            bat_file.write(f'''@echo off
python "{file_path}"
exit ''')
        print("Script added to system startup.")
    else:
        print("Script not added to system startup.")

if __name__ == "__main__":
    organize_downloads_folder()
    add_to_startup()
