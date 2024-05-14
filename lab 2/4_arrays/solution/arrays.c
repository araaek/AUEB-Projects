#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/**
 * Ylopoiiste ena programma pou tha dimiourgei kai tha emfanizei stin othoni ena pinaka tyxaiwn akeraiwn metaksy 
 * 1 kai 20.
 * To megethos tou pinaka tha dinetai apo ti grammi entolwn. Aparaitites synartiseis:
 * 1) int atoi(const char *nptr): The atoi() function converts the initial portion of the string pointed to by nptr to int.
 * 2) void *malloc(size_t size): The malloc() function allocates size bytes and returns a pointer to the allocated memory. 
 * The memory is not initialized. On error, returns NULL.
 * 3) void free(void *ptr): The free() function frees the memory space pointed to by ptr, 
 * which must have been returned by a previous call to malloc().
 * 4) void srand(unsigned int seed): The srand() function sets its argument as the seed for a new sequence of pseudo-random 
 * integers to be returned by rand(). These sequences are repeatable by calling srand() with the same seed value. 
 * 5) int rand(void): The rand() function returns a pseudo-random integer in the range 0 to RAND_MAX inclusive. If no seed value is 
 * provided, the rand() function is automatically seeded with a value of 1. 
*/
int main(int argc, char **argv) { 
	
	int arraySize, *randomArray, i;

	//dyo orismata (to prwto orisma einai to onoma tou programmatos).
	if (argc != 2) {
		printf("ERROR: Provide one argument.\n");
		return -1;
	}

	//xrisi tis atoi gia metatropi char * se int.
	arraySize = atoi(argv[1]);

	if (arraySize < 1 || arraySize > 20) {
		printf("ERROR: Please give a number between 1 and 20.\n");
		return -1;
	}

	printf("The array will have %d random integers.\n", arraySize);
	srand(time(NULL));
	
	//xrisi malloc gia dimiourgia tou pinaka me megethos arraySize.
	//desmeuoume sizeof(int) * arraySize sti mnimi.
	randomArray = (int *) malloc(sizeof(int) * arraySize);

	//elegxos an apetyxe i malloc
	if (randomArray == NULL) {
		printf("ERROR: Malloc failed not enough memory!\n");
		return -1;
	}

	//xrisi tis rand kai anathesi timwn ston pinaka.
	for (i = 0; i < arraySize; i++) {
		randomArray[i] = rand() % 20 + 1;
	}

	//emfanisi twn timwn tou pinaka
	for (i = 0; i < arraySize; i++) {
		printf("randomArray[%d] = %d.\n", i, *(randomArray + i));
	}

	//panta eletherwnoume ti mnimi pou exoume desmeusei.
    free(randomArray);

	return 0;
}            
