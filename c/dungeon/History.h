// Header file for the History data type
// DO NOT MODIFY!

#ifndef HISTORY_H
#define HISTORY_H

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

void historyInit(History* history);
void historyAdd(History* history, Action action);
void historyPrint(const History* history);
void historyUninit(History* history);               

#endif
