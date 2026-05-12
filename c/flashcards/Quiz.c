//Author: Fritz Geib
//Email: ftgeib@mtu.edu
//Description: flashcard quiz

#include <float.h>
#include <stdio.h>
#include <stdlib.h>
#include "Card.h"


int main(int argc, char** argv) {
    if (argc < 2) {
        printf("Usage: Quiz <in filename> <attempts> [out filename] \n");
        return 0;
    }

    FILE* fin = fopen(argv[1], "r");
    if (fin == NULL) {
        printf("ERROR: failed to open input file!\n");
        return 1;
    }

    int questions = atoi(argv[2]);
    if (questions <= 0) {
        printf("ERROR: attempts must be positive!\n");
        return 1;
    }

    int NUM_CARDS;
    fscanf(fin, "%d", &NUM_CARDS);
    Card cards[NUM_CARDS];
    double minScore, maxScore;
    int minI, maxI, correctCount, attempts;
    minI = maxI = -1;
    correctCount = attempts = 0;
    minScore = DBL_MAX;
    maxScore = 0.0;

    for (int i = 0; i < NUM_CARDS; i++) {
        char front[MAX_CARD_LEN + 1];
        char back[MAX_CARD_LEN + 1];
        int stack, correct, incorrect;
        fscanf(fin, "%255s %255s %d %d %d",
                front, back, &stack, &correct, &incorrect);
        initCard(&cards[i], front, back, stack, correct, incorrect);
        double score = correctPercentCard(&cards[i]);
        if (score < minScore) {
            minScore = score;
            minI = i;
        }
        if (score > maxScore) {
            maxScore = score;
            maxI = i;
        }
        correctCount += correct;
        attempts += correct + incorrect;
    }
    fclose(fin);

    printf("Cards read: %d\nPrevious attempts: %d (%.2f%% correct)", NUM_CARDS, attempts,
            attempts > 0 ? 100.0 * correctCount / attempts : 0.0);
    printf("\nEasiest card: ");
    printCard(&cards[maxI], false);
    printf("Hardest card: ");
    printCard(&cards[minI], false);

    int numCorrect = 0;
    for (int i = 0; i < questions; i++) {
        Card* card = &cards[0];
        for (int j = 1; j < NUM_CARDS; j++) {
            if (cards[j].stack < card->stack)
                card = &cards[j];
            if (cards[j].stack == card->stack && cards[j].seen < card->seen)
                card = &cards[j];
        }

        printf("#%d: %s? ", i+1, card->front);
        char answer[MAX_CARD_LEN+1];
        scanf("%255s", answer);
        if (checkAndUpdateCard(card, answer)) {
            printf("Correct!\n");
            numCorrect += 1;
        } else
            printf("Incorrect: %s\n", card->back);
    }

    printf("You answered %.2f%% correctly\n",
            numCorrect > 0 ? 100.0 * numCorrect / questions : 0.0);

    if (argc >= 3) {
        FILE* fout = fopen(argv[3], "w");
        if (fout == NULL) {
            printf("ERROR: failed to open output file\n");
            for (int i = 0; i < NUM_CARDS; i++)
                uninitCard(&cards[i]);
            return 1;
        }
        fprintf(fout, "%d\n", NUM_CARDS);
        for (int i = 0; i < NUM_CARDS; i++) {
            fprintf(fout, "%s %s %d %d %d\n",
                    cards[i].front, cards[i].back, cards[i].stack, cards[i].correct, cards[i].incorrect);
        }
        fclose(fout);
        printf("Wrote %d cards to output file\n", NUM_CARDS);
    }

    for (int i = 0; i < NUM_CARDS; i++)
        uninitCard(&cards[i]);

    return 0;
}
