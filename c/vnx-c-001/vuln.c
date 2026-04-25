// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-C-001: Unbounded string copy functions

#include <string.h>
#include <stdio.h>

void copy_username(char *dest, const char *src) {
    // TRIGGERS VNX-C-001: strcpy without bounds check
    strcpy(dest, src);
}

void append_domain(char *buf, const char *domain) {
    // TRIGGERS VNX-C-001: strcat without bounds check
    strcat(buf, domain);
}

void read_line(char *buf) {
    // TRIGGERS VNX-C-001: gets is always unsafe
    gets(buf);
}

void wide_copy(wchar_t *dst, const wchar_t *src) {
    // TRIGGERS VNX-C-001: wcscpy without bounds check
    wcscpy(dst, src);
}
