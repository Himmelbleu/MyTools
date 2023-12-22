from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog

import copy_multi_file


class OpenFileDialogThread(QtCore.QThread):
    updator = QtCore.pyqtSignal(str)
    file_type = "1"

    def run(self):
        if self.file_type == "1":
            options = QtWidgets.QFileDialog.Options()
            file_path, _ = QtWidgets.QFileDialog().getOpenFileName(None, "选择文件", "",
                                                                   "All Files (*)",
                                                                   options=options)
            self.updator.emit(file_path if file_path else '')
        else:
            options = QFileDialog.Options()
            folder_path = QFileDialog.getExistingDirectory(options=options)
            self.updator.emit(folder_path if folder_path else '')


class DecryptMultiFileThread(QtCore.QThread):
    updator = QtCore.pyqtSignal(dict)

    def __init__(self, source_folder, des_folder):
        super().__init__()
        self.source_folder = source_folder
        self.des_folder = des_folder

    def run(self):
        copy_multi_file.decrypt_multi_file(self.source_folder, self.des_folder, self.exe_callback)

    def exe_callback(self, file_count, file_total, source_file, des_file, e):
        self.updator.emit({
            'file_count': str(file_count),
            'progress': round((file_count / file_total) * 100),
            'source_file': source_file,
            'des_file': des_file,
            'text': f"第 {file_count} 个文件正在解密中.......\n",
            'e': e
        })
