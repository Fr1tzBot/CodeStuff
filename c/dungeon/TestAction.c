// Test program for the Action data type

#include "Action.h"
#include <stdio.h>

int main(void)
{
    // Test an invalid character, all the directions, and the quit command
    char chars[] = {'t', 'w', 's', 'a', 'd', 'q'};    
    for (int i = 0; i < 6; i++)
    {
        printf("'%c' -> %d\n", chars[i], actionFromChar(chars[i]));
    }
    printf("\n");
    
    Action actions[] = {ActionInvalid, ActionNorth, ActionSouth, ActionEast, ActionWest, ActionQuit};
    for (int i = 0; i < 6; i++)
    {
        printf("%d -> %s\n", i, actionToString(actions[i]));
    }
    printf("\n");

    for (int i = 0; i < 6; i++)
    {
        int deltaRow = 0;
        int deltaCol = 0;
        bool result = actionMoveDelta(actions[i], &deltaRow, &deltaCol);
        printf("%d -> %d %d %d\n", i, result, deltaRow, deltaCol);
    }
    
    return 0;
}
