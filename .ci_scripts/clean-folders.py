"""clean-folders.py

Script to clean everything in contributions folder

"""
from pathlib import Path
import shutil

HERE = Path(__file__).parent
BASE = HERE.parent.absolute()
MAIN_FOLDER = BASE / "contributions"

if __name__ == "__main__":
    print("🗑️ Starting folders clean up ...")
    for folder in MAIN_FOLDER.iterdir():
        if folder.name == '.gitkeep':
            continue
        if folder.is_dir():
            print(f"Deleting {folder}")
            shutil.rmtree(folder)
    print("✅ Done ...")
