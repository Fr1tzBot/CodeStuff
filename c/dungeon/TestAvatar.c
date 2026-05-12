// Test program for the Avatar data type

#include "Avatar.h"

#include <stdio.h>
#include <string.h>

int main(void)
{
    Avatar a1;  
    char name[256] = "Crocodile Dundee";
           
    // Test all the functions of the data type
    avatarInit(&a1, name);
    avatarDisplay(&a1);

    // Add 2 gems and 1 key
    avatarAddGem(&a1);
    avatarAddGem(&a1);
    avatarAddKey(&a1);
    avatarDisplay(&a1);
    
    // Use the one key we should have
    avatarUseKey(&a1);
    avatarDisplay(&a1);

    // Test using more keys then we have
    avatarUseKey(&a1);
    avatarDisplay(&a1);
    
    // Create a second Avatar with a long name and use the local string buffer
    Avatar a2;  
    strcpy(name, "The Great-great-grandson of Conan the Barbarian");
    avatarInit(&a2, name);
    avatarDisplay(&a2);

    // Avatar 1 should still display correctly.
    avatarDisplay(&a1);    
    
    // Avatar 2 should display correctly even after uninitalizing avatar 1
    avatarUninit(&a1);
    avatarDisplay(&a2);    

    avatarUninit(&a2);
    
    return 0;
}
