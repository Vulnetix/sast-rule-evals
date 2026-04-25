// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-JAVA-014: Java zip slip via ZipEntry getName()

import java.io.*;
import java.util.zip.*;
import java.nio.file.*;

public class ZipExtractor {

    public void extractZip(String zipFilePath, String destDir) throws IOException {
        ZipInputStream zis = new ZipInputStream(new FileInputStream(zipFilePath));
        ZipEntry entry;

        while ((entry = zis.getNextEntry()) != null) {
            // VULNERABLE: getName() used directly in new File() without traversal check
            File outFile = new File(destDir, entry.getName());

            // An attacker can set entry.getName() = "../../etc/cron.d/backdoor"
            FileOutputStream fos = new FileOutputStream(outFile);
            byte[] buffer = new byte[1024];
            int len;
            while ((len = zis.read(buffer)) > 0) {
                fos.write(buffer, 0, len);
            }
            fos.close();
            zis.closeEntry();
        }
        zis.close();
    }

    public void extractWithPaths(String zipFilePath, String destDir) throws IOException {
        ZipInputStream zis = new ZipInputStream(new FileInputStream(zipFilePath));
        ZipEntry entry;

        while ((entry = zis.getNextEntry()) != null) {
            // VULNERABLE: using Paths.get with getName() without validation
            Path target = Paths.get(destDir, entry.getName());
            Files.copy(zis, target);
            zis.closeEntry();
        }
        zis.close();
    }
}
