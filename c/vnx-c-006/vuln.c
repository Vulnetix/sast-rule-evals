// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-C-006: Use of alloca() for dynamic allocation

#include <alloca.h>
#include <string.h>
#include <stddef.h>

void process_input(size_t user_size) {
    // TRIGGERS VNX-C-006: alloca with runtime size - stack overflow if user_size is large
    char *buf = alloca(user_size);
    memset(buf, 0, user_size);
}

void build_path(const char *prefix, size_t len) {
    // TRIGGERS VNX-C-006: alloca inside a loop or with variable size
    char *path = alloca(len + 1);
    memcpy(path, prefix, len);
    path[len] = '\0';
}
