import glob
import os
from datetime import datetime

current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("""%Y-%m-%d %H_%M_%S""")

log_files = glob.glob("logs/*.txt")
with open("logs/merged_logs.txt", "a") as merged_file:
    files = 0
    #MERGING
    for file_name in log_files:
        files = files + 1
        with open(file_name, "r") as file:
            content = file.read()
            merged_file.writelines(content)
            print(f"#{files} filename: {file_name} compiled")
            print(content)
    delete = input(f"Confirm deleting of {files} files? (y/n)")
    deleted_files = 0
    #DELETING
    if delete == "y":
        for file_name in log_files:
            deleted_files = deleted_files + 1
            os.remove(file_name)
            print(f"#{deleted_files}/{files} filename: {file_name} deleted.")
    else:
        print("Cancelled")