// VNX-JAVA-012: LDAP injection
import javax.naming.directory.*;
import javax.servlet.http.*;

public class LdapSearch extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws Exception {
        DirContext ctx = null; // initialized elsewhere
        String user = request.getParameter("username");
        String filter = "(uid=" + request.getParameter("username") + ")";
        NamingEnumeration results = ctx.search("ou=users", filter, new SearchControls());
    }
}
