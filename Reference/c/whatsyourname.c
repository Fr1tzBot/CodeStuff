#include <stdio.h>
int main() {
    char firstName[100];
    printf("Type your first name: ");
    scanf("%s", &firstName);
    printf("Nice To Meet You %s!\n", firstName);
    return 0;
}