import java.sql.*;

// VNX-JAVA-003: SQL injection via string concatenation
public class SqlInjection {
    public User findUser(Connection conn, String username) throws SQLException {
        Statement stmt = conn.createStatement();
        ResultSet rs = stmt.executeQuery("SELECT * FROM users WHERE name = '" + username + "'");
        return null;
    }
}
