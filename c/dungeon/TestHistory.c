// Test program for the History data type

#include "History.h"
#include <stdio.h>

int main(void)
{
    Action actions[] = {ActionInvalid,
                        ActionNorth,
                        ActionSouth,
                        ActionEast,
                        ActionEast,
                        ActionWest,
                        ActionSouth,
                        ActionQuit};
    History history;

    historyInit(&history);
    for (int i = 0; i < 8; i++)
    {
        historyAdd(&history, actions[i]);
    }
    historyPrint(&history);
    historyUninit(&history);
    
    return 0;
}
