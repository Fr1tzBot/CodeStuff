// Test program for the Tile data type

#include "Tile.h"
#include <stdio.h>

int main(void)
{
    // Test out mapping characters in the input file to the Tile data type
    char chars[] = {'t', '.', '#', '-', '=', 'S', '*', '+'};    
    for (int i = 0; i < 8; i++)
    {
        printf("'%c' -> %d\n", chars[i], tileFromChar(chars[i]));
    }
    printf("\n");
    
    // Test out displaying all possible Tile types
    Tile tiles[] = {TileInvalid, TileEmpty, TileWall, TileDoor, TileLockedDoor, TileSecretPassage, TileGem, TileKey};
    for (int i = 0; i < 8; i++)
    {
        printf("%d -> '", i);
        tileDisplay(tiles[i]);
        printf("'\n");
    }
    printf("\n");

    // Test out whether each tile type is passable or not
    for (int i = 0; i < 8; i++)
    {
        printf("%d -> %d\n", i, tilePassable(tiles[i]));
    }
        
    return 0;
}
