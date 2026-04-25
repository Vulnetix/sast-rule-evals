// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-JAVA-025: Hardcoded password or credential in source code

import java.sql.Connection;
import java.sql.DriverManager;

public class HardcodedPassword {

    // TRIGGERS: hardcoded password literal
    private static final String DB_PASSWORD = "SuperSecret123!";

    // TRIGGERS: hardcoded passwd literal
    private String passwd = "admin@password";

    public Connection getConnection() throws Exception {
        // TRIGGERS: DriverManager.getConnection with inline credentials
        return DriverManager.getConnection(
            "jdbc:mysql://localhost:3306/appdb",
            "root",
            "rootPassword123"
        );
    }

    public void configure() {
        // TRIGGERS: pwd assignment from string literal
        String pwd = "hardcoded_service_password";
        System.setProperty("service.password", pwd);
    }
}
