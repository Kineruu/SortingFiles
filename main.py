
import time
import os

"""
Start of the project ~19:45 CEST, 09/04/2026 (9th April 2026)
"""

current_path = input("Enter folder's path: ")

if os.path.exists(current_path): 
    pass
else:
    print("That path does not exist!")
    quit()

def sort_by_date():
    number = 1
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
                
                while os.path.exists(new_full_path):
                    new_item_name = f"{readable_time}_{number}{get_extension}"
                    new_full_path = os.path.join(current_path, new_item_name)
                    number += 1

                os.rename(full_path, new_full_path)
        print("Sorted.")
        input()

    except FileNotFoundError: print("The file does not exist.")

def format_size(size_in_bytes, option):
    if option == 1: return f"{size_in_bytes} B"
    elif option == 2: return f"{size_in_bytes / 1024:.2f} KB"
    elif option == 3: return f"{size_in_bytes / (1024 ** 2):.2f} MB"
    elif option == 4: return f"{size_in_bytes / (1024 ** 3):.2f} GB"
    else: return f"{size_in_bytes} B"

def sort_by_size():
    number = 1
    try: size_format = int(input("1. B\n2. KB\n3. MB\n4. GB\nOPTION: "))
    except ValueError: size_format = 3

    try:
        files = os.listdir(current_path)
        for item in files:
            full_path = os.path.join(current_path, item)

            if os.path.isfile(full_path):
                get_file_size = os.path.getsize(full_path)

                readable_size = format_size(get_file_size, size_format)
                get_extension = os.path.splitext(item)[1]
                new_item_name = f"{readable_size}{get_extension}"
                new_full_path = os.path.join(current_path, new_item_name)
                
                while os.path.exists(new_full_path):
                    new_item_name = f"{readable_size}_{number}{get_extension}"
                    new_full_path = os.path.join(current_path, new_item_name)
                    number += 1

                os.rename(full_path, new_full_path)

        print("Sorted.")
        input()

    except FileNotFoundError: print("The file does not exist.")    

if __name__ == "__main__":
    get_user_option = int(input("1. Sort by date\n2. Sort by size\nOPTION: "))
    if get_user_option == 1: sort_by_date()
    if get_user_option == 2: sort_by_size()
    if get_user_option not in (1, 2): quit()

