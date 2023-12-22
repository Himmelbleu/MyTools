import os
import shutil


def decrypt_signal_file(source_file, des_folder, callback):
    try:
        if not os.path.exists(des_folder):
            os.makedirs(des_folder)

        shutil.copy(source_file, des_folder)
        callback({
            'source_file': source_file,
            'des_folder': des_folder
        })
    except (shutil.Error, OSError) as e:
        callback({
            'source_file': source_file,
            'des_folder': des_folder,
            'e': e
        })
