// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-JAVA-027: Spring security headers disabled (clickjacking, CSP)

import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;

@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        // TRIGGERS: frameOptions disabled — enables clickjacking
        http
            .authorizeRequests().anyRequest().authenticated()
            .and()
            .httpBasic()
            .and()
            .headers()
                .frameOptions().disable()  // X-Frame-Options removed
            .and()
            .csrf().disable();
    }

    // Alternative misconfiguration: all security headers disabled
    protected void configureBad(HttpSecurity http) throws Exception {
        // TRIGGERS: entire headers() block disabled
        http.headers().disable();
    }
}
