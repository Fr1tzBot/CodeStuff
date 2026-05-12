//Author: Fritz Geib
//Email: ftgeib@mtu.edu
//Description: helpers for interacting with flash card structs

#include <stdbool.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#define MAX_CARD_LEN 255

// How many stacks used for the algorithm
#define NUM_STACKS 3

typedef struct
{
    char* front;    // String appearing on front side of card
    char* back;     // String appearing on back side of card
    int stack;      // Stack the card is in, lower the number the harder the card
    int correct;    // Lifetime correct attempts
    int incorrect;  // Lifetime incorrect attempts
    int seen;       // Attempts during current quiz
} Card;

void initCard(Card* card, const char* front, const char* back, int stack, int correct, int incorrect) {
    card->front = malloc(sizeof(char) * (MAX_CARD_LEN + 1));
    card->back  = malloc(sizeof(char) * (MAX_CARD_LEN + 1));
    strcpy(card->front, front);
    strcpy(card->back, back);
    card->stack = stack;
    card->correct = correct;
    card->incorrect = incorrect;
    card->seen = 0;
}

void uninitCard(Card* card) {
    free(card->front);
    free(card->back);
}

double correctPercentCard(const Card* card) {
    if (card->incorrect == 0 && card->correct == 0)
        return 0.0;

    return 100.0 * card->correct / (card->correct + card->incorrect);
}
void printCard(const Card* card, bool verbose) {
    if (verbose)
        printf("%s -> %s (%.2f%%), correct=%d, incorrect=%d, stack=%d, seen=%d\n",
                card->front, card->back, correctPercentCard(card),
                card->correct, card->incorrect, card->stack, card->seen);
    else
        printf("%s -> %s (%.2f%%)\n", card->front, card->back, correctPercentCard(card));
}

bool checkAndUpdateCard(Card* card, const char* answer) {
    bool correct = strcmp(card->back, answer) == 0;
    card->seen += 1;
    card->correct +=   correct ? 1 : 0;
    card->incorrect += correct ? 0 : 1;

    if (card->stack < NUM_STACKS - 1 && correct)
        card->stack += 1;

    if (card->stack > 0 && !correct)
        card->stack -= 1;

    return correct;
}
