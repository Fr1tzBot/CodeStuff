//Author: Fritz Geib
//Email: ftgeib@mtu,edu
//Description: A program where the user guesses a number 1-100

#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int main(int argc, char* argv[])
{
    // Seed the random number generator with the number of seconds since 1970

    int num;
    if (argc > 1) {
        num = atoi(argv[1]);
    } else {
        srand(time(NULL));
        num = rand() % 100 + 1;
    }

    int i;
    int guess;
    for (i = 1; ; i++) {
        printf("Number? ");
        scanf("%d", &guess);
        printf("You entered %d.\n", guess);
        if (guess < 1 || guess > 100) {
            printf("Invalid input!\n"); continue;
        }

        int off = abs(guess - num);
        if (off == 0) {
            printf("You nailed it!\n");
            break;
        } else if (off == 1) {
            printf("On fire.\n");
        } else if (off <= 5) {
            printf("Hot.\n");
        } else if (off <= 10) {
            printf("Getting warmer.\n");
        } else if (off <= 19) {
            printf("Cold.\n");
        } else {
            printf("Ice cold.\n");
        }
    }
    printf("It took you %d guesses\n", i);

    return 0;
}
