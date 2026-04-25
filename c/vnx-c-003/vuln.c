// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-C-003: OS command injection via system()/popen()

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void run_user_command(const char *filename) {
    char cmd[512];
    snprintf(cmd, sizeof(cmd), "process %s", filename);
    // TRIGGERS VNX-C-003: system() with non-literal argument
    system(cmd);
}

FILE *open_pipe(const char *user_arg) {
    char cmd[256];
    snprintf(cmd, sizeof(cmd), "grep %s /etc/log", user_arg);
    // TRIGGERS VNX-C-003: popen() with non-literal argument
    return popen(cmd, "r");
}

// Safe: literal commands are lower risk
void safe_command(void) {
    system("ls /tmp");
}
