#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define SIZE (1024 * 1024) // 1M elements (approx 8MB RAM)
#define ITERS 10000000     // 10M accesses

struct Node {
    struct Node *next;
    int pad[14]; // Pad to 64 bytes (typical cache line size) to prevent false sharing/prefetching benefits
};

struct Node pool[SIZE];

int main() {
    // 1. Initialize nodes linearly
    for (int i = 0; i < SIZE - 1; i++) {
        pool[i].next = &pool[i + 1];
    }
    pool[SIZE - 1].next = &pool[0];

    // 2. Randomize the links (Fisher-Yates shuffle)
    // This makes the memory access pattern unpredictable
    srand(time(NULL));
    for (int i = SIZE - 1; i > 0; i--) {
        int j = rand() % (i + 1);
        struct Node *temp = pool[i].next;
        pool[i].next = pool[j].next;
        pool[j].next = temp;
    }

    // 3. The Benchmark Loop
    struct Node *current = &pool[0];
    volatile struct Node *dummy; // volatile to prevent optimization
    
    printf("Starting pointer chase...\n");
    for (int i = 0; i < ITERS; i++) {
        current = current->next;
    }
    
    // Prevent dead code elimination
    dummy = current;
    printf("Done.\n");
    return 0;
}