//Author: Fritz Geib
//Email: ftgeib@mtu.edu
//Description: flashcard parser and flipper
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

//Lowercases alphabetic characters in the string in place
void lowercase(char* str) {
    int selected = 0;
     do {
        if (str[selected] >= 'A' && str[selected] <= 'Z')
            str[selected] += ('a'-'A');
    } while (str[selected += 1] != '\0');
}

int main(int argc, char** argv) {
    int mode;
    if (argc > 1)
        mode = atoi(argv[1]);
    else
        mode = 0;

    //Bools:
    //Reverse?
    //Zero Reversed Cards?
    //Zero existing Cards?
    bool reverse, zero_reversed, zero_existing;
    switch (mode) {
        case 1:
            reverse = true;
            zero_reversed = true;
            zero_existing = false;
            break;
        case 2:
            reverse = true;
            zero_reversed = true;
            zero_existing = true;
            break;
        case 3:
            reverse = true;
            zero_reversed = false;
            zero_existing = false;
            break;
        default:
            reverse = false;
            zero_reversed = false;
            zero_existing = false;
            break;
    }


    int NUM_CARDS = 0;
    scanf("%d", &NUM_CARDS);
    printf("%d\n", NUM_CARDS * (reverse ? 2 : 1));

    for (int i = 0; i < NUM_CARDS; i++) {
        char front[256];
        char back[256];
        char* frontp = (char*) &front;
        char* backp = (char*) &back;
        int stack;
        int correct;
        int incorrect;
        scanf("%255s %255s %d %d %d",
              frontp, backp, &stack, &correct, &incorrect);

        lowercase(frontp);
        lowercase(backp);
        if (zero_existing) {
            stack = 0;
            correct = 0;
            incorrect = 0;
        }

        printf("%s %s %d %d %d\n",
                front, back, stack, correct, incorrect);

        if (reverse)
            printf("%s %s %d %d %d\n",
                    back, front,
                    zero_reversed ? 0 : stack,
                    zero_reversed ? 0 : correct,
                    zero_reversed ? 0 : incorrect);
    }
}
