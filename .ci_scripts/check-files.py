"""check-files.py

Script to check on files that changed and author of files.

"""
import argparse
import sys

ALLOWED_FOLDER = "contributions"
ADMIN_USERS = ["lsetiawan"]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run check file for appropriate structure")
    parser.add_argument("touchedfiles", metavar="TOUCHED_FILES", type=str)
    parser.add_argument("author", metavar="FILE_AUTHOR", type=str)
    args = parser.parse_args()
    file_list = args.touchedfiles.split(",")

    # author must match folder
    file_author = args.author

    print("=== Checking files ===")
    for idx, f in enumerate(file_list):
        if (f"{ALLOWED_FOLDER}/{file_author}" in f) or (file_author in ADMIN_USERS):
            print(f"{idx}) PASSED: {f}.")
            continue
        else:
            print(f"{idx}) FAILED: {f} not allowed!")
            print("=== FAILED. Please try again. ===")
            sys.exit(1)
    print("=== Done. All good. ===")
