// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-CS-007: Path traversal via Path.Combine with user input

using System.IO;
using Microsoft.AspNetCore.Mvc;

public class FileServer : Controller
{
    private readonly string _uploadsDir = "/var/www/uploads";

    // VULNERABLE: Path.Combine with request parameter, no validation
    public IActionResult Download(string filename)
    {
        // Request.Query["filename"] could be "../../etc/passwd"
        var filePath = Path.Combine(_uploadsDir, Request.Query["filename"]);
        var bytes = File.ReadAllBytes(filePath);
        return File(bytes, "application/octet-stream");
    }

    // VULNERABLE: Path.Combine with form data
    public IActionResult ServeTemplate(string name)
    {
        var templatePath = Path.Combine("templates", Request.Form["name"]);
        var content = File.ReadAllText(templatePath);
        return Content(content);
    }
}
