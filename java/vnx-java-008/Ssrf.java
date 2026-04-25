// VNX-JAVA-008: Server-side request forgery
import java.net.*;
import javax.servlet.http.*;

public class Ssrf extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String target = request.getParameter("url");
        URL url = new URL(request.getParameter("target"));
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.getInputStream();
    }
}
