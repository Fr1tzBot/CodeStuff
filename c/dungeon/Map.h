// Header file for the Map data type
// DO NOT MODIFY!

#ifndef MAP_H
#define MAP_H

#include <stdbool.h>

#include "Tile.h"
#include "Action.h"
#include "Avatar.h"

typedef struct
{
    int rows;           // Vertical size of the Map 
    int cols;           // Horizontal size of the Map
    Tile** tiles;       // 2D array of Tile structures      
    int avatarRow;      // Current row of the Avatar on the Map
    int avatarCol;      // Current column of the avatar on map  
    int gemsRemaining;  // How many gems are left on the map   
} Map;

bool mapInit(Map* map, const char* filename);
void mapUninit(Map* map);
void mapDisplay(const Map* map);
bool mapMoveAvatar(Map* map, Avatar* avatar, Action action);

#endif
