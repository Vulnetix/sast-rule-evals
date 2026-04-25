// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-C-004: Use-after-free

#include <stdlib.h>
#include <string.h>

typedef struct { int value; } Node;

void process_node(Node *node) {
    free(node);
    // TRIGGERS VNX-C-004: accessing node->value after free
    node->value = 0;
}

int get_value_after_free(Node *n) {
    free(n);
    // TRIGGERS VNX-C-004: returning freed pointer
    return n->value;
}
