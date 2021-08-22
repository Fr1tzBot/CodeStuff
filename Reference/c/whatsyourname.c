#include <stdio.h>
int main() {
    int foo = 8;
    char aString[] = "yeet";
    char firstName[100];
    printf("Type your first name: ");
    scanf("%s", &firstName);
    printf("Nice To Meet You, ");
    printf("%s", firstName);
    printf("!\n");
    return 0;
}