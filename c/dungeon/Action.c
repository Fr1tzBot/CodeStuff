//Name: Fritz Geib
//Email: ftgeib@mtu.edu
//Desc: utilities for working with actions

#include <stdbool.h>

typedef enum {ActionInvalid, ActionNorth, ActionSouth, ActionEast, ActionWest, ActionQuit} Action;
Action actionFromChar(char ch) {
    switch (ch) {
        case 'w':
            return ActionNorth;
        case 's':
            return ActionSouth;
        case 'd':
            return ActionEast;
        case 'a':
            return ActionWest;
        case 'q':
            return ActionQuit;
        default:
            return ActionInvalid;
    }
}

const char* actionToString(Action a) {
    //Possible strings are: "invalid", "north", "south", "east", "west", "quit".
    switch (a) {
        case ActionInvalid:
            return "invalid";
        case ActionNorth:
            return "north";
        case ActionSouth:
            return "south";
        case ActionEast:
            return "east";
        case ActionWest:
            return "west";
        case ActionQuit:
            return "quit";
    }
}

bool actionMoveDelta(Action a, int* deltaRow, int* deltaCol) {
    switch (a) {
        case ActionInvalid:
        case ActionQuit:
            return false;
        case ActionNorth:
            *deltaRow += -1;
            break;
        case ActionSouth:
            *deltaRow += 1;
            break;
        case ActionEast:
            *deltaCol += 1;
            break;
        case ActionWest:
            *deltaCol += -1;
            break;
    }
    return true;
}

