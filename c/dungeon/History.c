//Name: Fritz Geib
//Email: ftgeib@mtu.edu
//Desc: utilities for working with history

#include <stdio.h>
#include <stdlib.h>
#include "Action.h"

typedef struct node
{
    Action action;       // Action taken by the user
    struct node* next;   // Next node in the linked list
} Node;

typedef struct
{
    Node*  first;        // Pointer to the first node in list of actions taken
    Node*  last;        // Pointer to last node in linked list of actions taken
} History;

void historyInit(History* history) {
    history->first = NULL;
    history->last = NULL;
}

void historyAdd(History* history, Action action) {

    Node* newNode = malloc(sizeof(Node));
    newNode->action = action;
    newNode->next = NULL;

    if (history->last == NULL)
        history->first = newNode;
    else
        history->last->next = newNode;
    history->last = newNode;
}

void historyPrint(const History* history) {
    Node* selected = history->first;
    do
        printf("%s ", actionToString(selected->action));
    while ((selected = selected->next) != NULL);
    printf("\n");
}

void freeNode(Node* sel) {
    if (sel->next != NULL)
        freeNode(sel->next);
    free(sel);
}

void historyUninit(History* history) {
    freeNode(history->first);
    history->first = NULL;
    history->last = NULL;
}










