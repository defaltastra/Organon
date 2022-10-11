import os
import glob
import shutil
# mapping each extension with its corresponding folder
# For example, 'jpg', 'png', 'ico', 'gif', 'svg' files will be moved to 'images' folder
# feel free to change based on your needs
extensions = {
    "jpg": "images",
    "png": "images",
    "ico": "images",
    "gif": "images",
    "svg": "images",
    "sql": "sql",
    "exe": "programs",
    "msi": "programs",
    "pdf": "pdf",
    "xlsx": "excel",
    "csv": "excel",
    "rar": "archive",
    "zip": "archive",
    "gz": "archive",
    "tar": "archive",
    "7z":"archive",
    "docx": "word",
    "torrent": "torrent",
    "txt": "text",
    "ipynb": "python",
    "py": "python",
    "pptx": "powerpoint",
    "ppt": "powerpoint",
    "mp3": "audio",
    "wav": "audio",
    "mp4": "video",
    "m3u8": "video",
    "webm": "video",
    "ts": "typescript",
    "json": "json",
    "css": "web",
    "js": "web",
    "html": "web",
    "apk": "apk",
    "sqlite3": "sqlite3",
}
qst = print("Organizing Downloads Folder...")
time.sleep(1)
USER_NAME = getpass.getuser()
#Add to startup function
def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.abspath(__file__)
        file_path2 = f"C:\\Users\\{name}\\Documents"
        file_path3 = f"C:\\Users\\{name}\\Documents\\Organon.py"
        try:
            shutil.copy(file_path , file_path2)
        except shutil.SameFileError:
                pass
        

    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(f'''@echo off
python "{file_path3}"
pause ''')
        
if __name__ == "__main__":
    name = os.getlogin()
    path = f"C:\\Users\\{name}\\Downloads"
    verbose = 1
    for extension, folder_name in extensions.items():
        # get all the files matching the extension
        files = glob.glob(os.path.join(path, f"*.{extension}"))
        if verbose == 1
            print(f"[*] Found {len(files)} files with {extension} extension")
        if not os.path.isdir(os.path.join(path, folder_name)) and files:
            # create the folder if it does not exist before
            print(f"[+] Making {folder_name} folder")
            os.mkdir(os.path.join(path, folder_name))
        for file in files:
            # for each file in that extension, move it to the correponding folder
            basename = os.path.basename(file)
            dst = os.path.join(path, folder_name, basename)
            if verbose == 1:
                print(f"[*] Moving {file} to {dst}")
            shutil.move(file, dst)
add_to_startup()
