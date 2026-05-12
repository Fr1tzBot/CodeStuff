// Test harness for the Card data type.
// This tets the public API of the data type, 
// You can modify this if you want for your own testing purposes.
// You don't need to submit this source file to Canvas, it will not be graded.

#include <stdio.h>
#include <stdlib.h>

#include "Card.h"

// Create a null-terminated string with size-1 letters
void fill(int size, char str[size])
{
    for (int i = 0; i < size - 1; i++)
    {
        str[i] = 'A' + (i % 26);
    }
    str[size - 1] = '\0';
}

int main(void)
{
    int test = 0;

    // Test 1, card with no correct attempts
    printf("*** Test %d\n", ++test);
    Card c1;
    initCard(&c1, "red", "rojo", 0, 0, 9);
    printCard(&c1, false);
    printf("correct = %.4f\n", correctPercentCard(&c1));
    uninitCard(&c1);

    // Test 2, card with mostly correct attempts, but don't uninit it yet
    printf("*** Test %d\n", ++test);
    Card c2;
    initCard(&c2, "blue", "azul", 0, 4, 1);
    printCard(&c2, true);
    printf("correct = %.4f\n", correctPercentCard(&c2));

    // Test 3, card with no attempts at all and blank strings
    printf("*** Test %d\n", ++test);
    initCard(&c1, "", "", 1, 0, 0);
    printCard(&c1, false);
    printf("correct = %.4f\n", correctPercentCard(&c2));

    // Uninit both cards
    uninitCard(&c1);
    uninitCard(&c2);

    // Test 4, card with one big string and big counts
    printf("*** Test %d\n", ++test);
    char str[MAX_CARD_LEN + 1];
    fill(MAX_CARD_LEN + 1, str);
    initCard(&c1, str, "super-big!!!", 2, 1234, 4567);
    initCard(&c2, "also_super_big!!!", str, 2, 4567, 1234);
    printCard(&c1, false);
    printf("correct = %.4f\n", correctPercentCard(&c1));
    printCard(&c2, false);
    printf("correct = %.4f\n", correctPercentCard(&c2));
    uninitCard(&c2);
    uninitCard(&c1);

    // Create two cards in an array
    Card cards[2];
    const char* answers[] = {"one", "Two"};
    initCard(&cards[0], "uno", "one", 0, 0, 0);
    initCard(&cards[1], "dos", "two", 2, 0, 0);

    // Test 5, getting a card correct multiple times, then wrong, then correct, then wrong again
    printf("*** Test %d\n", ++test);
    printCard(&cards[0], true);
    for (int loops = 0; loops < 3; loops++)
    {
        // Correct guess
        printf("guess '%s'=%d, ", answers[0], checkAndUpdateCard(&cards[0], answers[0]));
        printCard(&cards[0], true);
    }
    // Wrong guess
    printf("guess '%s'=%d, ", answers[1], checkAndUpdateCard(&cards[0], answers[1]));
    printCard(&cards[0], true);
    // Correct guess
    printf("guess '%s'=%d, ", answers[0], checkAndUpdateCard(&cards[0], answers[0]));
    printCard(&cards[0], true);    
    // Wrong guess x 2
    printf("guess '%s'=%d, ", answers[1], checkAndUpdateCard(&cards[0], answers[1]));
    printCard(&cards[0], true);    
    printf("guess '%s'=%d, ", answers[1], checkAndUpdateCard(&cards[0], answers[1]));
    printCard(&cards[0], true);    

    // Test 6, demoting the other card with wrong guesses
    printf("*** Test %d\n", ++test);
    printCard(&cards[1], true);    
    printf("guess '%s'=%d, ", answers[1], checkAndUpdateCard(&cards[1], answers[1]));
    printCard(&cards[1], true);    
    printf("guess '%s'=%d, ", answers[1], checkAndUpdateCard(&cards[1], answers[1]));
    printCard(&cards[1], true);    
    printf("guess '%s'=%d, ", answers[1], checkAndUpdateCard(&cards[1], answers[1]));
    printCard(&cards[1], true);    

    uninitCard(&cards[0]);
    uninitCard(&cards[1]);

    return 0;
}
