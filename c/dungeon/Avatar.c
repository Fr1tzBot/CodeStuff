//Name: Fritz Geib
//Email: ftgeib@mtu.edu
//Desc: utilities for working with avatars

#include <stdbool.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

typedef struct
{
    char* name;   // Name of the Avatar
    int gems;     // Gems collected by the avatar thus far
    int keys;     // Keys currently held by the avatar
} Avatar;

void avatarInit(Avatar* avatar, const char* name) {
    avatar->gems = 0;
    avatar->keys = 0;
    avatar->name = malloc(strlen(name) + 1);
    strcpy(avatar->name, name);
}

void avatarUninit(Avatar* avatar) {
    free(avatar->name);
    // free(avatar);
    avatar = NULL; //Pretty sure this does nothing
}

bool avatarUseKey(Avatar* avatar) {
    if (avatar->keys > 0) {
        avatar->keys -= 1;
        return true;
    } else
        return false;
}

void avatarAddKey(Avatar* avatar) {
    avatar->keys += 1;
}

void avatarAddGem(Avatar* avatar) {
    avatar->gems += 1;
}

void avatarDisplay(const Avatar* avatar) {
    printf("%s's inventory: gems %d, keys %d\n",
            avatar->name, avatar->gems, avatar->keys);
}
















