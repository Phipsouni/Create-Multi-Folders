import os
import time
import sys

def create_folders_in_directory(directory, folder_names_file):
    with open(folder_names_file, 'r') as file:
        names_list = file.readlines()
        for index, name in enumerate(names_list, start=1):
            folder_name = name.strip()
            folder_name_with_number = f"{index}_{folder_name}"
            folder_path = os.path.join(directory, folder_name_with_number)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.readline().strip()

if __name__ == "__main__":
    main_folder = read_file('path.txt')
    folder_names_file = "foldernames.txt"
    create_folders_in_directory(main_folder, folder_names_file)
    print("Создание папок завершено")
    time.sleep(3)
    sys.exit()
