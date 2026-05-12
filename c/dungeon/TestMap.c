// Test program for the Map data type

#include "Map.h"
#include "Action.h"

#include <stdio.h>

int main(void)
{
    // First test trying to load a bad filename
    Map mapBad;
    const char* badFilename = "bogus.txt";
    printf("init of '%s' = %d\n", badFilename, mapInit(&mapBad, badFilename));
 
    // Now test with one of the provided test files
    Map mapGood;
    const char* goodFilename = "tiny.txt";
    printf("init of '%s' = %d\n", goodFilename, mapInit(&mapGood, goodFilename));

    // Test display and gem count 
    mapDisplay(&mapGood);
    printf("gems remaining = %d\n", mapGood.gemsRemaining);
    
    // Test a sequence of actions that tries to move off all sides of the map
    // Also test the non-movement actions
    Action actions[] = {ActionSouth, ActionNorth, ActionNorth, ActionNorth, ActionEast, ActionEast, ActionWest, ActionWest, ActionWest, ActionWest, ActionQuit, ActionInvalid};
    
    Avatar avatar;
    avatarInit(&avatar, "Conan");
    
    for (int i = 0; i < 12; i++)
    {
        printf("move %d -> %d\n", actions[i], mapMoveAvatar(&mapGood, &avatar, actions[i]));
    }
    printf("gems remaining = %d\n", mapGood.gemsRemaining);

    avatarUninit(&avatar);
    mapUninit(&mapGood);
    
    return 0;
}
