import os
import shutil


def decrypt_signal_file(source_file, destination_folder, fnc):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    shutil.copy(source_file, destination_folder)
    fnc(source_file, destination_folder)
