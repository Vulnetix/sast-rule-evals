// VNX-JAVA-010: Spring CSRF disabled
import org.springframework.security.config.annotation.web.builders.HttpSecurity;

public class SecurityConfig {
    protected void configure(HttpSecurity http) throws Exception {
        http.csrf().disable()
            .authorizeRequests()
            .anyRequest().authenticated();
    }
}
