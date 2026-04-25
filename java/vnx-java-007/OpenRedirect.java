// VNX-JAVA-007: Open redirect
import javax.servlet.http.*;

public class OpenRedirect extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String url = request.getParameter("url");
        response.sendRedirect(request.getParameter("next"));
    }
}
