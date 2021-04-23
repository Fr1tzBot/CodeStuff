#include <stdio.h>
int main() {
    bool condition = true;
    while (condition) {
        printf("foo\n");
        break;
    }
    return 0;
}