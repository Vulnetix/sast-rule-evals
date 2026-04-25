// VNX-JAVA-011: Expression language injection
import org.springframework.expression.spel.standard.SpelExpressionParser;
import javax.servlet.http.*;

public class SpelInjection extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws Exception {
        SpelExpressionParser parser = new SpelExpressionParser();
        String expr = request.getParameter("expr");
        Object result = parser.parseExpression(request.getParameter("expr")).getValue();
    }
}
