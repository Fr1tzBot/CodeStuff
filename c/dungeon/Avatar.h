// Header file for the Avatar data type
// DO NOT MODIFY!

#ifndef AVATAR_H
#define AVATAR_H

#include <stdbool.h>

typedef struct
{
    char* name;   // Name of the Avatar
    int gems;     // Gems collected by the avatar thus far
    int keys;     // Keys currently held by the avatar   
} Avatar;

void avatarInit(Avatar* avatar, const char* name);
void avatarUninit(Avatar* avatar);
bool avatarUseKey(Avatar* avatar);
void avatarAddKey(Avatar* avatar);
void avatarAddGem(Avatar* avatar);
void avatarDisplay(const Avatar* avatar);

#endif

