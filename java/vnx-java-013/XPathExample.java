// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-JAVA-013: Java XPath injection

import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathFactory;
import javax.servlet.http.HttpServletRequest;

public class XPathExample {

    public String findUser(HttpServletRequest request, org.w3c.dom.Document doc) throws Exception {
        String username = request.getParameter("username");

        XPathFactory factory = XPathFactory.newInstance();
        XPath xpath = factory.newXPath();

        // VULNERABLE: user input concatenated directly into XPath expression
        String expression = "//users/user[name='" + username + "']";
        return xpath.evaluate(expression, doc);
    }

    public boolean authenticate(HttpServletRequest request, org.w3c.dom.Document doc) throws Exception {
        String user = request.getParameter("user");
        String pass = request.getParameter("pass");

        XPathFactory factory = XPathFactory.newInstance();
        XPath xpath = factory.newXPath();

        // VULNERABLE: can bypass auth with: ' or '1'='1
        String query = "//users/user[name='" + user + "' and password='" + pass + "']";
        return xpath.evaluate(query, doc) != null;
    }
}
