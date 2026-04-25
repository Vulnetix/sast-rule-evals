// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-KOTLIN-003: Cookie missing HttpOnly flag in Kotlin

import javax.servlet.http.Cookie
import javax.servlet.http.HttpServletResponse

class CookieController {

    fun setSessionCookie(response: HttpServletResponse, sessionId: String) {
        val cookie = Cookie("JSESSIONID", sessionId)
        cookie.maxAge = 3600
        // TRIGGERS: HttpOnly explicitly disabled
        cookie.setHttpOnly(false)
        response.addCookie(cookie)
    }

    fun setRememberMeCookie(response: HttpServletResponse, token: String) {
        val cookie = Cookie("rememberMe", token)
        cookie.maxAge = 86400
        // TRIGGERS: addCookie without setHttpOnly
        response.addCookie(cookie)
    }
}
