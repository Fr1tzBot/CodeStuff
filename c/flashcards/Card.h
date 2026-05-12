#ifndef _CARD_H_
#define _CARD_H_
// DO NOT MODIFY!

#include <stdbool.h>

// Maximum number characters of the string on front or back of a card
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

void initCard(Card* card, const char* front, const char* back, int stack, int correct, int incorrect);
void uninitCard(Card* card);
double correctPercentCard(const Card* card);
void printCard(const Card* card, bool verbose);
bool checkAndUpdateCard(Card* card, const char* answer);

#endif
