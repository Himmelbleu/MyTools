import os
import shutil


def count_files_in_directory(directory):
    if not os.path.exists(directory):
        return 0

    file_count = 0
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            file_count += 1
        elif os.path.isdir(item_path):
            file_count += count_files_in_directory(item_path)
    return file_count


def decrypt_multi_file(source_folder, des_folder, callback):
    file_total = count_files_in_directory(source_folder)
    file_count = 0
    if not os.path.exists(des_folder):
        os.makedirs(des_folder)

    for root, dirs, files in os.walk(source_folder):
        des_root = root.replace(source_folder, des_folder, 1)
        if not os.path.exists(des_root):
            os.makedirs(des_root)

        for file in files:
            source_file = os.path.join(str(root), str(file))
            des_file = os.path.join(str(des_root), str(file))
            shutil.copy2(source_file, des_file)
            file_count += 1
            callback(file_count, file_total, source_file, des_file)
