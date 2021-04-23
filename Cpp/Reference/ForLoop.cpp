#include <stdio.h>
int main() {
    int arrayToIndexThrough[] = { 1, 2, 4, 8, 16, 32, 64, 128 };
    int i;
    //Index through an array
    for (i=0; i<(sizeof(arrayToIndexThrough)/sizeof(*arrayToIndexThrough)); i++){
        printf("%d\n", arrayToIndexThrough[i]);
    }
    //Repeat a set number of times (10)
    for (i=1; i<=10; i++){
        printf("%d\n", i);
    }
}