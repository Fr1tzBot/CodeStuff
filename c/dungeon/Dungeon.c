// main program for the Dungeon game
// DO NO MODIFY!

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <ctype.h>     // For tolower() function

#include "Map.h"
#include "Avatar.h"
#include "Action.h"
#include "History.h"

// Helper function to read in a line of text dropping any line ending
int readLine(int n, char str[n])
{
   int ch;
   int i = 0;
   while (((ch = getchar()) != '\n') && (ch != '\r') && (ch != EOF))
   {
      if (i < n - 1)
      {
         str[i] = ch;
         i++;
      }
   }
   str[i] = '\0';
   return i;
}

// Helper function for reading in next command
Action readNextAction(void)
{
    int ch = 0;
    
    // Discard line endings
    while (((ch = getchar()) != EOF) && ((ch == '\n') || (ch == '\r')))
    {   
    }

    // If we reach end of file, treat as a quit action
    if (ch == EOF)
    {
        return ActionQuit;
    }
    
    return actionFromChar(tolower(ch));    
}

// Main program that runs the Dungeon game
int main(int argc, char** argv)
{
    int level = 1;
    
    if (argc < 2)
    {
        printf("Usage: Dungeon <level 1 filename> [level 2 filename] ...\n");
        return 0;
    }    
    
    const int maxLevel = argc - 1;

    // Read in up to 99 characters, ensure buffer gets null terminated
    char str[100];
    printf("What is your name? ");
    readLine(100, str);
           
    Map map;
    Avatar avatar;
    History history;
    
    avatarInit(&avatar, str);

    Action action = ActionInvalid;
    int move = 1;
    
    // Outer loop handles multiple levels
    do
    {
        printf("You enter dungeon level %d!\n", level);    
        if (!mapInit(&map, argv[level]))
        {
            printf("Failed to load file '%s'\n", argv[level]);
            avatarUninit(&avatar);
            return 1;
        }
        historyInit(&history);
        
        while ((action != ActionQuit) && (map.gemsRemaining > 0))
        {
            mapDisplay(&map);
            avatarDisplay(&avatar);
            
            // Print move number and prompt for user
            printf("%d: Command? ", move);
            move++;
            
            action = readNextAction();
            historyAdd(&history, action);
            
            if (action != ActionQuit)
            {
                // Try and move in the given direction
                if (!mapMoveAvatar(&map, &avatar, action))
                {
                    // Opps, move didn't work must have hit a wall or something
                    printf("Bonk!\n");
                }
            }                        
            printf("\n");
        }
        
        // Free up any resources for this level
        mapUninit(&map);

        // Print the move history for this level
        printf("Moves: ");
        historyPrint(&history);

        // Free up the history for this level
        historyUninit(&history);
        
        level++;
    }
    while ((action != ActionQuit) && (level <= maxLevel));
    
    if (action != ActionQuit)
    {
        printf("You escaped the dungeon!\n");    
    }
    
    avatarUninit(&avatar);
    
    return 0;
}
