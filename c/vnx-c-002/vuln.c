// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-C-002: Format string injection

#include <stdio.h>
#include <syslog.h>

void log_user_action(const char *user_input) {
    // TRIGGERS VNX-C-002: printf with user-controlled format string
    printf(user_input);
}

void log_error(const char *msg) {
    // TRIGGERS VNX-C-002: fprintf with variable as format argument
    fprintf(stderr, msg);
}

void syslog_event(int priority, const char *event) {
    // TRIGGERS VNX-C-002: syslog with variable format
    syslog(priority, event);
}

// Safe: literal format strings are fine
void safe_log(const char *user_input) {
    printf("%s\n", user_input);
    fprintf(stderr, "%s\n", user_input);
}
