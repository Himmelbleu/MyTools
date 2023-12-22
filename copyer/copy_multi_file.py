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
    file_total = sum(len(files) for _, _, files in os.walk(source_folder))
    file_count = 0
    try:
        # 遍历源文件夹
        for root, dirs, files in os.walk(source_folder):
            # 获取相对路径
            relative_path = os.path.relpath(root, source_folder)
            # 构建目标文件夹中的对应路径
            target_folder = os.path.join(des_folder, relative_path)

            # 确保目标文件夹存在，如果不存在则创建
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            # 复制文件并将内容写入对应的目标文件
            for file in files:
                src_file_path = os.path.join(root, file)
                dst_file_path = os.path.join(target_folder, file)

                with open(src_file_path, 'rb') as source_file:
                    with open(dst_file_path, 'wb') as des_file:
                        content = source_file.read()
                        des_file.write(content)

                file_count += 1
                callback(file_count, file_total, source_folder, des_folder, '')
    except (shutil.Error, OSError) as e:
        callback(file_count, file_total, source_folder, des_folder, e)
