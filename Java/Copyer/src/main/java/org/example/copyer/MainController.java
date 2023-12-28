package org.example.copyer;

import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.control.TextArea;
import javafx.scene.input.Dragboard;
import javafx.scene.input.TransferMode;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;

public class MainController {

    private final StringBuilder message = new StringBuilder();
    @FXML
    private Label dragFileArea;
    @FXML
    private TextArea textArea;

    @FXML
    private void initialize() {
        dragFileArea.setOnDragOver(event -> {
            if (event.getGestureSource() != dragFileArea && event.getDragboard().hasFiles()) {
                event.acceptTransferModes(TransferMode.COPY_OR_MOVE);
            }
            event.consume();
        });

        dragFileArea.setOnDragDropped(event -> {
            Dragboard db = event.getDragboard();
            DirectoryCopier co = new DirectoryCopier();
            boolean success = false;
            if (db.hasFiles()) {
                success = true;
                String filePath;
                for (File file : db.getFiles()) {
                    filePath = file.getAbsolutePath();
                    message.append(filePath).append("\n");
                    if (file.isDirectory()) {
                        try {
                            co.copyFolder(new File(filePath), new File(filePath + co.getSuffix()));
                        } catch (IOException e) {
                            throw new RuntimeException(e);
                        }
                    } else {
                        try (InputStream inputStream = new FileInputStream(file)) {
                            byte[] data = inputStream.readAllBytes();
                            co.copyFile(file, data);
                        } catch (IOException e) {
                            e.fillInStackTrace();
                        }
                    }
                }
                textArea.setText(message.toString());
            }
            event.setDropCompleted(success);
            event.consume();
        });
    }

}