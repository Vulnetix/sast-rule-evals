// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-C-005: Integer overflow in malloc/calloc size

#include <stdlib.h>
#include <stddef.h>

void *alloc_records(size_t count, size_t elem_size) {
    // TRIGGERS VNX-C-005: multiplication in malloc size - may overflow
    return malloc(count * elem_size);
}

void *resize_buffer(void *ptr, size_t old_size, size_t extra) {
    // TRIGGERS VNX-C-005: addition in realloc size - may overflow
    return realloc(ptr, old_size + extra);
}

void *alloc_matrix(size_t rows, size_t cols) {
    // TRIGGERS VNX-C-005: multiplication in malloc
    char *matrix = malloc(rows * cols * sizeof(double));
    return matrix;
}
