
import time
import os

"""
Start of the project ~19:45 CEST, 09/04/2026 (9th April 2026)

TODO:
Sort files by:
-> Date,
-> Size,
-> Extension,
-> Name
"""

current_path = input("Enter folder's path: ")

def sort_by_date():
    try:
        files = os.listdir(current_path)
        for item in files:
            full_path = os.path.join(current_path, item)
            if os.path.isfile(full_path):
                created_time = os.path.getctime(full_path)
                readable_time = time.strftime("%d-%m-%Y_%H-%M-%S", time.localtime(created_time))

                get_extension = os.path.splitext(item)[1]
                new_item_name = f"{readable_time}{get_extension}"
                new_full_path = os.path.join(current_path, new_item_name)
                
                if not os.path.exists(new_full_path):
                    os.rename(full_path, new_full_path)

    except FileNotFoundError:
        print("The file does not exist.")

sort_by_date()

