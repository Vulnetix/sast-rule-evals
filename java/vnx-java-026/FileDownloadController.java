// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-JAVA-026: Spring file serving without access control

import org.springframework.core.io.FileSystemResource;
import org.springframework.core.io.InputStreamResource;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.io.*;
import java.nio.file.*;

@RestController
@RequestMapping("/files")
public class FileDownloadController {

    private static final String BASE_DIR = "/var/app/uploads/";

    @GetMapping("/{filename}")
    public ResponseEntity<FileSystemResource> download(
            @PathVariable String filename) {
        // TRIGGERS: FileSystemResource from @PathVariable without authorisation check
        Path filePath = Paths.get(BASE_DIR).resolve(filename);
        return ResponseEntity.ok(new FileSystemResource(filePath));
    }

    @GetMapping("/stream")
    public ResponseEntity<InputStreamResource> stream(
            @RequestParam("path") String path) throws IOException {
        // TRIGGERS: InputStreamResource from @RequestParam without authorisation check
        InputStream is = new FileInputStream(path);
        return ResponseEntity.ok(new InputStreamResource(is));
    }
}
