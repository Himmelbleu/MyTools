        self.decrypt_signal_file.toggled.connect(self.on_radio_button_toggled)
        self.decrypt_multi_files.toggled.connect(self.on_radio_button_toggled)

        self.signal_file_selector_btn.clicked.connect(self.on_signal_file_selector)
        self.signal_file_decrypt_dest_dir_selector_btn.clicked.connect(self.on_signal_file_decrypt_des_dir_selector)
        self.start_decrypt_signal_file.clicked.connect(self.on_start_decrypt_signal_file)

        self.multi_file_dir_selector_btn.clicked.connect(self.on_multi_file_dir_selector_btn)
        self.multi_file_decrypt_dest_dir_selector_btn.clicked.connect(self.on_multi_file_decrypt_des_dir_selector)
        self.start_decrypt_multi_file.clicked.connect(self.on_start_decrypt_multi_file)

    def on_radio_button_toggled(self):
        if self.decrypt_signal_file.isChecked():
            self.stackedWidget.setCurrentIndex(0)
        elif self.decrypt_multi_files.isChecked():
            self.stackedWidget.setCurrentIndex(1)

    def on_signal_file_selector(self):
        self.open_file_dialog_thread = OpenFileDialogThread()
        self.open_file_dialog_thread.updator.connect(lambda x: {
            self.signal_file_label.setText(x)
        })
        self.open_file_dialog_thread.file_type = "1"
        self.open_file_dialog_thread.start()

    def on_signal_file_decrypt_des_dir_selector(self):
        self.open_file_dialog_thread = OpenFileDialogThread()
        self.open_file_dialog_thread.updator.connect(lambda x: {
            self.signal_file_dest_dir_label.setText(x)
        })
        self.open_file_dialog_thread.file_type = "2"
        self.open_file_dialog_thread.start()

    def on_start_decrypt_signal_file(self):
        copy_signal_file.decrypt_signal_file(self.signal_file_label.text(),
                                             self.signal_file_dest_dir_label.text(),
                                             lambda source_file, destination_folder: {
                                                 self.signal_file_textarea.append(
                                                     f"文件 '{source_file}' 已复制到目标目录 '{destination_folder}' 中。\n")
                                             })

    def on_multi_file_dir_selector_btn(self):
        self.open_file_dialog_thread = OpenFileDialogThread()
        self.open_file_dialog_thread.updator.connect(lambda x: {
            self.multi_file_dir_label.setText(x)
        })
        self.open_file_dialog_thread.file_type = "2"
        self.open_file_dialog_thread.start()

    def on_multi_file_decrypt_des_dir_selector(self):
        self.open_file_dialog_thread = OpenFileDialogThread()
        self.open_file_dialog_thread.updator.connect(lambda x: {
            self.multi_file_dest_dir_label.setText(x)
        })
        self.open_file_dialog_thread.file_type = "2"
        self.open_file_dialog_thread.start()

    def on_start_decrypt_multi_file(self):
        source_folder = self.multi_file_dir_label.text()
        des_folder = self.multi_file_dest_dir_label.text()
        self.decrypt_multi_file_thread = DecryptMultiFileThread(source_folder, des_folder)
        self.decrypt_multi_file_thread.updator.connect(self.after_decrypt_multi_file_thread_signal)
        self.decrypt_multi_file_thread.start()

    def after_decrypt_multi_file_thread_signal(self, data):
        self.multi_file_decrypt_progress.setValue(data['progress'])
        self.multi_file_num.setText(data['file_count'])
        self.multi_file_textarea.append(data['text'])