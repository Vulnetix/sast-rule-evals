// VNX-JAVA-009: Path traversal
import java.io.*;
import javax.servlet.http.*;

public class PathTraversal extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String filename = request.getParameter("file");
        File f = new File(request.getParameter("path"));
        FileInputStream fis = new FileInputStream(f);
    }
}
