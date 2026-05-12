# Starter makefile for flashcards assignment.
# This will build the UpdateCards and TestCard executables.
# You need to add support for building Quiz executable.
#
# NOTE: Submit your updated makefile with your other source files!

CC = gcc
CFLAGS = -std=c99 -pedantic -Wall -Wextra -O1 -fsanitize=address
LDFLAGS = -lm

default: UpdateCards TestCard Quiz

UpdateCards: UpdateCards.c Card.h
	${CC} ${CFLAGS} UpdateCards.c -o UpdateCards ${LDFLAGS}

TestCard: TestCard.c Card.o
	${CC} ${CFLAGS} TestCard.c Card.o -o TestCard ${LDFLAGS}

Card.o: Card.c Card.h
	${CC} ${CFLAGS} -c Card.c

Quiz: Quiz.c Card.o
	${CC} ${CFLAGS} Quiz.c Card.o -o Quiz ${LDFLAGS}

clean:
	rm -f UpdateCards TestCard *.o Quiz
