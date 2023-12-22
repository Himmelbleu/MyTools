import os
import shutil


def decrypt_multi_file(source_folder, destination_folder, fnc):
    count = 0
    # 如果目标文件夹不存在，则创建
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # 遍历源文件夹中的文件和文件夹
    for root, dirs, files in os.walk(source_folder):
        # 创建目标文件夹中的对应子文件夹
        dest_root = root.replace(source_folder, destination_folder, 1)
        if not os.path.exists(dest_root):
            os.makedirs(dest_root)

        # 复制文件
        for file in files:
            source_file = os.path.join(root, file)
            dest_file = os.path.join(dest_root, file)
            shutil.copy2(source_file, dest_file)
            count += 1
            fnc(count, files, source_file, dest_file)
