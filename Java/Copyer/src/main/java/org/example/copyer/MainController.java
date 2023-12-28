package org.example.copyer;

import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.input.Dragboard;
import javafx.scene.input.TransferMode;
import javafx.scene.layout.VBox;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;

public class MainController {

    @FXML
    private VBox root;

    @FXML
    private Label filePathText;

    @FXML
    private void initialize() {
        root.setOnDragOver(event -> {
            if (event.getGestureSource() != root && event.getDragboard().hasFiles()) {
                event.acceptTransferModes(TransferMode.COPY_OR_MOVE);
            }
            event.consume();
        });

        root.setOnDragDropped(event -> {
            Dragboard db = event.getDragboard();
            boolean success = false;
            if (db.hasFiles()) {
                success = true;
                String filePath = null;
                for (File file : db.getFiles()) {
                    filePath = file.getAbsolutePath();
                    try (InputStream inputStream = new FileInputStream(file)) {
                        byte[] data = inputStream.readAllBytes();
                        // 这里可以处理获取到的二进制数据 data
                        System.out.println("File path: " + filePath);
                        System.out.println("Binary data: " + bytesToHex(data)); // 将二进制数据转换成十六进制字符串输出
                    } catch (IOException e) {
                        e.fillInStackTrace();
                    }
                }
                filePathText.setText("文件路径: " + filePath);
            }
            event.setDropCompleted(success);
            event.consume();
        });
    }

    private static String bytesToHex(byte[] bytes) {
        StringBuilder hexString = new StringBuilder();
        for (byte aByte : bytes) {
            String hex = Integer.toHexString(0xff & aByte);
            if (hex.length() == 1) {
                hexString.append('0');
            }
            hexString.append(hex);
        }
        return hexString.toString();
    }

}