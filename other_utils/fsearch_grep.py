#!/usr/bin/env python3

import os
import subprocess

def search_file(directory, search_phrase, search_option=None):
        count = 0
        if directory == "~" or directory =="":
                directory = os.getcwd()
        elif not directory:
                directory = os.getcwd()

        if not os.path.isdir(directory):
                print(f"{directory} is not a valid directory")
                return
        print(f"Searching for the phrase '{search_phrase}' in {directory}...")
        if not search_option or search_option == "":
            # Search only in the specified directory (no subdirectories)
            for file in os.listdir(directory):
                file_path = os.path.join(directory, file)
                if os.path.isfile(file_path):  # Only process files
                    try:
                        result = subprocess.run(
                            ['grep', '-H', search_phrase, file_path],
                            capture_output=True, text=True
                        )
                        if result.returncode == 0:  # grep returns 0 if it finds a match
                            count += 1
                            print(f"\033[1;33mFound log file: {file} => {file_path}\033[0m")
                            print(f"\033[1;32m--- Matching Lines in {file} ---\033[0m")
                            print(result.stdout)  # Output the matching lines from grep
                            print(f"\033[1;32m--- EOF of {file} ---\033[0m")
                    except Exception as e:
                        print(f"Error reading file {file_path}: {e}")

        else:
            # Search recursively through subdirectories
            for root, dirs, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        result = subprocess.run(
                            ['grep', '-H', search_phrase, file_path],
                            capture_output=True, text=True
                        )
                        if result.returncode == 0:  # grep returns 0 if it finds a match
                            count += 1
                            print(f"\033[1;33mFound log file: {file} => {file_path}\033[0m")
                            print(f"\033[1;32m--- Matching Lines in {file} ---\033[0m")
                            print(result.stdout)  # Output the matching lines from grep
                            print(f"\033[1;32m--- EOF of {file} ---\033[0m")
                    except Exception as e:
                        print(f"Error reading file {file_path}: {e}")

        # else:
        #     print("Invalid option! Please choose '1' for subdirectories or 'None' for the current directory.")

        print(f"\n\033[1;31m--- {count} files found with the search term ---\033[0m")

if __name__=="__main__":
        directory = input("Where to search..(path)?: ")
        search_phrase = input("Enter phrase: ")
        search_option = input("Choose option: 1 for subdirs, None for dir only!: ")
        search_file(directory, search_phrase, search_option)