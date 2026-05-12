// Header file for the Action data type
// DO NOT MODIFY!

#ifndef ACTION_H
#define ACTION_H

#include <stdbool.h>
   
// Represents an input action from the user of the game
typedef enum {ActionInvalid, ActionNorth, ActionSouth, ActionEast, ActionWest, ActionQuit} Action;  

Action actionFromChar(char ch);
const char* actionToString(Action a);
bool actionMoveDelta(Action a, int* deltaRow, int* deltaCol);       

#endif


