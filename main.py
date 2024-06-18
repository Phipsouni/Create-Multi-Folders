import os

def create_folders_in_directory(directory, folder_names_file):
    with open(folder_names_file, 'r') as file:
        names_list = file.readlines()
        for index, name in enumerate(names_list, start=1):
            folder_name = name.strip()
            folder_name_with_number = f"{index}_{folder_name}"
            folder_path = os.path.join(directory, folder_name_with_number)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

if __name__ == "__main__":
    with open('mainfolder.txt', 'r') as file:
        main_folder = file.readline().strip()
    folder_names_file = "foldernames.txt"
    create_folders_in_directory(main_folder, folder_names_file)
