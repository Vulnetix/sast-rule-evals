// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-JAVA-022: Insecure temporary file creation

import java.io.File;
import java.io.IOException;

public class InsecureTempFile {

    public File createReport(String userId) throws IOException {
        // TRIGGERS: File.createTempFile with world-readable permissions
        File tempFile = File.createTempFile("report_", ".pdf");
        tempFile.deleteOnExit();
        return tempFile;
    }

    public File processUpload(String userId) throws IOException {
        // TRIGGERS: predictable path under /tmp/ with user-controlled suffix
        File tempFile = new File("/tmp/" + userId + "_upload.tmp");
        tempFile.createNewFile();
        return tempFile;
    }

    public void writeConfig(String appName, String configData) throws IOException {
        // TRIGGERS: predictable /tmp/ path via concatenation
        File config = new File("/tmp/" + appName + ".conf");
        config.createNewFile();
    }
}
