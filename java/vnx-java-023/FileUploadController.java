// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-JAVA-023: Unrestricted file upload without content-type validation

import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
@RequestMapping("/upload")
public class FileUploadController {

    private static final String UPLOAD_DIR = "/var/app/uploads/";

    @PostMapping("/avatar")
    public String uploadAvatar(@RequestParam("file") MultipartFile file) throws IOException {
        // TRIGGERS: getOriginalFilename() used with Files.copy — no extension/MIME check
        String filename = file.getOriginalFilename();
        Files.copy(file.getInputStream(), Paths.get(UPLOAD_DIR + filename));
        return "Uploaded: " + filename;
    }

    @PostMapping("/document")
    public String uploadDocument(@RequestParam("doc") MultipartFile doc) throws IOException {
        // TRIGGERS: getOriginalFilename() with no content-type validation
        String originalName = doc.getOriginalFilename();
        doc.transferTo(Paths.get(UPLOAD_DIR).resolve(originalName));
        return "Saved: " + originalName;
    }
}
