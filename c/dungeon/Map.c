//Name: Fritz Geib
//Email: ftgeib@mtu.edu
//Desc: utilities for working with map

#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include "Tile.h"
#include "Avatar.h"
#include "Action.h"

#define INDEX(row, col, num_cols) ((row) * (num_cols) + (col))

typedef struct
{
    int rows;           // Vertical size of the Map
    int cols;           // Horizontal size of the Map
    Tile** tiles;       // 2D array of Tile structures
    int avatarRow;      // Current row of the Avatar on the Map
    int avatarCol;      // Current column of the avatar on map
    int gemsRemaining;  // How many gems are left on the map
} Map;

bool mapInit(Map* map, const char* filename) {
    map->gemsRemaining = 0;

    FILE* f = fopen(filename, "r");
    if (f == NULL) return false;

    //No error checking here since we are guaranteed to be given a valid file
    fscanf(f, "%d %d", &map->rows, &map->cols);
    fscanf(f, "%d %d", &map->avatarRow, &map->avatarCol);

    map->tiles = malloc(sizeof(Tile*) * map->rows * map->cols);
    if (map->tiles == NULL) {
        fclose(f);
        return false;
    }

    for (int i = 0; i < map->rows * map->cols; i++) {
        Tile* newTile;
        if ((newTile = malloc(sizeof(Tile))) == NULL) {
            for (int j = i - 1; j >= 0; j--)
                free(map->tiles[j]);
            free(map->tiles);
            fclose(f);
            return false;
        }

        char tmp;
        fscanf(f, " %c", &tmp);
        if (tileFromChar(tmp) == TileGem)
            map->gemsRemaining += 1;
        *newTile = tileFromChar(tmp);
        map->tiles[i] = newTile;
    }

    fclose(f);

    return true;
}

void mapUninit(Map* map) {
    for (int i = 0; i < map->cols * map->rows; i++)
        free(map->tiles[i]);
    free(map->tiles);
}

void mapDisplay(const Map* map) {
    for (int i = 0; i < map->rows * map ->cols; i++) {
        if (i/map->cols == map->avatarRow && i % map->cols == map->avatarCol)
            printf("@");
        else
            tileDisplay(*map->tiles[i]);
        if ((i+1) % map->cols == 0)
            printf("\n");
    }
}

bool mapMoveAvatar(Map* map, Avatar* avatar, Action action) {
    int dx = map->avatarRow;
    int dy = map->avatarCol;
    if (!actionMoveDelta(action, &dx, &dy))
        return false;

    if (dx < 0 || dy < 0 || dx >= map->rows || dy >= map->cols)
        return false;

    Tile* targetTile = map->tiles[INDEX(dx, dy, map->cols)];

    if (*targetTile == TileLockedDoor && avatarUseKey(avatar))
        *targetTile = TileDoor;


    if (*targetTile == TileGem) {
        avatarAddGem(avatar);
        map->gemsRemaining -= 1;
        *targetTile = TileEmpty;
    }

    if (*targetTile == TileKey) {
        avatarAddKey(avatar);
        *targetTile = TileEmpty;
    }

    //This catches still-locked doors
    if (!tilePassable(*targetTile))
        return false;

    map->avatarRow = dx;
    map->avatarCol = dy;

    return true;
}










