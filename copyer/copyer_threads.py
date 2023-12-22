from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog


class OpenFileDialogThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(str, name='OpenFileDialogThread')
    file_type = "1"

    def run(self):
        if self.file_type == "1":
            options = QtWidgets.QFileDialog.Options()
            file_path, _ = QtWidgets.QFileDialog().getOpenFileName(None, "选择文件", "",
                                                                   "All Files (*)",
                                                                   options=options)
            if file_path:
                self.signal.emit(file_path)
        else:
            options = QFileDialog.Options()
            folder_path = QFileDialog.getExistingDirectory(options=options)

            if folder_path:
                self.signal.emit(folder_path)
