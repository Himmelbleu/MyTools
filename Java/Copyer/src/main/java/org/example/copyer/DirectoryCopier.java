package org.example.copyer;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;

public class DirectoryCopier {

    private String suffix = "decrypted";
    private Integer fileCount = 0;

    public String getSuffix() {
        return suffix;
    }

    public void setSuffix(String suffix) {
        this.suffix = suffix;
    }

    public Integer getFileCount() {
        return fileCount;
    }

    public void setFileCount(Integer fileCount) {
        this.fileCount = fileCount;
    }

    public void copyFolder(File source, File target) throws IOException {
        if (source.isDirectory()) {
            if (!target.exists()) {
                target.mkdir();
            }

            String[] pathnameList = source.list();
            if (pathnameList != null) {
                for (String pathname : pathnameList) {
                    File srcFile = new File(source, pathname);
                    File destFile = new File(target, pathname);
                    fileCount++;
                    copyFolder(srcFile, destFile);
                }
            }
        } else {
            Path sourcePath = source.toPath();
            Path targetPath = target.toPath();
            Files.copy(sourcePath, targetPath, StandardCopyOption.REPLACE_EXISTING);
        }
    }

    public void copyFile(File file, byte[] data) throws IOException {
        String directoryPath = file.getParent();
        String filepath = directoryPath + File.separator + suffix + file.getName();

        try (FileOutputStream outputStream = new FileOutputStream(filepath)) {
            outputStream.write(data);
        }
    }

}
