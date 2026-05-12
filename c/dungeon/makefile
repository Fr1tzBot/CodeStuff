# makefile for the dungeon assignment

# These variables control the specifics of the compilation
CC = gcc
CFLAGS = -std=c99 -pedantic -Wall -Wextra -O1 -fsanitize=address
LDFLAGS = -lm

# When you type "make", it will default to trying to build all the programs
default: TestAction TestTile TestAvatar TestMap TestHistory Dungeon

# To build just the TestAction executable, type "make TestAction"
TestAction: TestAction.c Action.o
	${CC} ${CFLAGS} TestAction.c Action.o -o TestAction ${LDFLAGS}

# To build just the TestTile executable, type "make TestTile"
TestTile: TestTile.c Tile.o
	${CC} ${CFLAGS} TestTile.c Tile.o -o TestTile ${LDFLAGS}

# To build just the TestAvatar executable, type "make TestAvatar"
TestAvatar: TestAvatar.c Avatar.o
	${CC} ${CFLAGS} TestAvatar.c Avatar.o -o TestAvatar ${LDFLAGS}

# To build just the TestMap executable, type "make TestMap"
TestMap: TestMap.c Map.o Avatar.o Tile.o Action.o
	${CC} ${CFLAGS} TestMap.c Map.o Avatar.o Tile.o Action.o -o TestMap ${LDFLAGS}

# To build just the TestHistory executable, type "make TestHistory"
TestHistory: TestHistory.c History.o Action.o
	${CC} ${CFLAGS} TestHistory.c History.o Action.o -o TestHistory ${LDFLAGS}

# To build just the Dungeon executable, type "make Dungeon"
Dungeon: Dungeon.c Map.o Avatar.o Tile.o Action.o History.o
	${CC} ${CFLAGS} Dungeon.c Map.o Avatar.o Tile.o Action.o History.o -o Dungeon ${LDFLAGS}

# Builds just the object file for the Action data type
Action.o: Action.c Action.h
	${CC} ${CFLAGS} -c Action.c

# Builds just the object file for the Tile data type
Tile.o: Tile.c Tile.h
	${CC} ${CFLAGS} -c Tile.c

# Builds just the object file for the Avatar data type
Avatar.o: Avatar.c Avatar.h
	${CC} ${CFLAGS} -c Avatar.c

# Builds just the object file for the Map data type
Map.o: Map.c Map.h Action.h Tile.h
	${CC} ${CFLAGS} -c Map.c

# Builds just the object file for the History data type
History.o: History.c History.h Action.h
	${CC} ${CFLAGS} -c History.c

run: Dungeon
	./Dungeon

clean:
	rm -f TestAction TestTile TestAvatar TestMap TestHistory Dungeon *.o

