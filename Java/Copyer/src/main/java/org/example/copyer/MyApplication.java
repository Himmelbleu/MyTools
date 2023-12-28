package org.example.copyer;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;

public class MyApplication extends Application {

    public static void main(String[] args) {
        launch();
    }

    @Override
    public void start(Stage stage) throws IOException {
        FXMLLoader loader = new FXMLLoader(MyApplication.class.getResource("main-view.fxml"));
        Scene scene = new Scene(loader.load(), 320, 240);
        stage.setTitle("文件解密");
        stage.setScene(scene);
        stage.show();
    }

}