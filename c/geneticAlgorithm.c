#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

int POP_COUNT, ITER_COUNT, SEED;
char *IN_FILE;
char *OUT_FILE;

int DOLLAR_TOTAL;
int GENE_COUNT;
int * VALUES;

bool USE_LOG = false;
FILE* out;

bool read_equation(void) {
    FILE* f;
    f = fopen(IN_FILE, "r");
    if (f == NULL) { return false; }
    fscanf(f, "%d", &DOLLAR_TOTAL);
    fscanf(f, "%d", &GENE_COUNT);
    int b = -1;
    VALUES = malloc(GENE_COUNT * sizeof(int));
    for (int i = 0; fscanf(f, "%d ", &b) == 1; i++) {
        VALUES[i] = b;
    }
    fclose(f);
    return true;
}

FILE * read_log(void) {
    FILE* f;
    f = fopen(OUT_FILE, "w");
    return f;
}

int find_total(int counts[GENE_COUNT]){
    int total = 0;
    for (int i = 0; i < GENE_COUNT; i++) {
        total += VALUES[i] * counts[i];
    }
    return total;
}

int get_fitness(int counts[GENE_COUNT]) {
    return abs(find_total(counts) - DOLLAR_TOTAL);
}

//Returns the index of the max (worst fitness) member
int max(int population[POP_COUNT][GENE_COUNT], bool return_index) {
    int max_fitness = get_fitness(population[0]);
    int index = 0;
    for (int i = 1; i < POP_COUNT; i++) {
        int fitness = get_fitness(population[i]);
        if (fitness > max_fitness) {
            max_fitness = fitness;
            index = i;
        }

    }
    if (return_index) { return index; }
    else { return max_fitness; }
}

//Returns the index of the min (best fitness) member
int min(int population[POP_COUNT][GENE_COUNT], bool return_index) {
    int min_fitness = get_fitness(population[0]);
    int index = 0;
    for (int i = 1; i < POP_COUNT; i++) {
        int fitness = get_fitness(population[i]);
        if (fitness < min_fitness) {
            min_fitness = fitness;
            index = i;
        }

    }
    if (return_index) { return index; }
    else { return min_fitness; }
}

int rand_num(int max) {
    return rand() % max;
}


double average_population(int population[POP_COUNT][GENE_COUNT]) {
    double sum = 0.0;
    for (int i = 0; i < POP_COUNT; i++) {
        sum += get_fitness(population[i]);
    }
    return sum / POP_COUNT;
}

void copy(int source[], int dest[]) {
    for (int i = 0; i < GENE_COUNT; i++) {
        dest[i] = source[i];
    }
}


void print_eq(void) {
    for (int i = 0; i < GENE_COUNT; i++) {
        if (i != 0) { fprintf(out, " + "); }
        fprintf(out, "%d*x_%d", VALUES[i], i);
    }
    fprintf(out, " = %d\n", DOLLAR_TOTAL);
}

void print_member(int member[], bool toscreen) {
    FILE* f = out;
    if (toscreen && USE_LOG) { f = stdout; }
    for (int i = 0; i < GENE_COUNT; i++) {
        fprintf(f, "%d", member[i]);
    }
    fprintf(f, ", fitness=%d",
        get_fitness(member)
    );
}

void print_pop(int gen, int population[POP_COUNT][GENE_COUNT]) {
        fprintf(out, "*** Generation %d ***\n", gen);
        for (int j = 0; j < POP_COUNT; j++) {
            fprintf(out, "%d: ", j);
            print_member(population[j], false);
        fprintf(out, "\n");
        }

        fprintf(out, "avg=%.4lf, min=%d, max=%d\n",
                average_population(population),
                min(population, false),
                max(population, false)
        );
}

int error(char * msg) {
    printf("%s\n", msg);
    return 1;
}


int main(int argc, char *argv[]) {
    if (argc > 6 || argc < 5) {
        return error("Usage: GA <individuals> <max steps> <seed> <in file> [out file]");
    }
    POP_COUNT = atoi(argv[1]); //individuals
    if (POP_COUNT < 1) { return error("ERROR: individuals must be positive!"); }
    ITER_COUNT = atoi(argv[2]); //max steps
    SEED = atoi(argv[3]); //seed
    IN_FILE = argv[4]; //TODO: read info from IN_FILE
    if (argc == 6) {
        USE_LOG = true;
        OUT_FILE = argv[5];
    }

    out = stdout;
    if (!read_equation()) { return error("ERROR: failed to open in file!");}
    print_eq();
    int population[POP_COUNT][GENE_COUNT];
    srand(SEED);
    if (USE_LOG) {
        out = read_log();
        if (out == NULL) { return error("ERROR: failed to open log file!"); }
    }
    //Generate generation zero
    for (int i = 0; i < POP_COUNT; i++) {
        for (int j = 0; j < GENE_COUNT; j++) {
            population[i][j] = rand_num(10);
        }
    }

    print_pop(0, population);
    int i;
    for (i = 0; i < ITER_COUNT; i++) {
        int WORST_INDEX = max(population, true);

        //Ensure our source index isn't also our destination
        int MUT_INDEX = rand_num(POP_COUNT);
        int GENE_INDEX = rand_num(GENE_COUNT);
        int NEW_GENE = rand_num(10);
        // int mutated[GENE_COUNT] = population[MUT_INDEX];
        int mutated[GENE_COUNT];
        copy(population[MUT_INDEX], mutated);
        mutated[GENE_INDEX] = NEW_GENE;
        // population[WORST_INDEX] = mutated;
        copy(mutated, population[WORST_INDEX]);
        fprintf(out, "Mutated individual %d -> %d, changed gene %d to %d\n",
            MUT_INDEX, WORST_INDEX, GENE_INDEX, NEW_GENE
        );
        print_pop(i+1, population);
        if (min(population, false) == 0) { break; }
    }

    int best_index = min(population, true);
    printf("BEST %d: ", best_index);
    print_member(population[best_index], true);
    printf(", steps=%d\n", i);

    free(VALUES);
    return 0;
}
