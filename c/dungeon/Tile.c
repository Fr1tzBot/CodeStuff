#include <stdbool.h>
#include <stdio.h>

typedef enum {TileInvalid, TileEmpty, TileWall, TileDoor, TileLockedDoor, TileSecretPassage, TileGem, TileKey} Tile;

Tile tileFromChar(char ch) {
    if (ch == '.')
        return TileEmpty;
    if (ch == '#')
        return TileWall;
    if (ch == '-')
        return TileDoor;
    if (ch == '=')
        return TileLockedDoor;
    if (ch == 'S')
        return TileSecretPassage;
    if (ch == '*')
        return TileGem;
    if (ch == '+')
        return TileKey;
    return TileInvalid;
}

void tileDisplay(Tile tile) {
    if (tile == TileEmpty)
        printf(" ");
    if (tile == TileWall || tile == TileSecretPassage)
        printf("#");
    if (tile == TileDoor)
        printf("-");
    if (tile == TileLockedDoor)
        printf("=");
    if (tile == TileGem)
        printf("*");
    if (tile == TileKey)
        printf("+");
}

bool tilePassable(Tile tile) {
    if (tile == TileInvalid || tile == TileWall || tile == TileLockedDoor)
        return false;
    else
        return true;
}
