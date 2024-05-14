#include "my_functions.h"

/**
 * Synartisi pou antistrefei tis times twn dyo akeraiwn pou dinontai
 * san orismata.
 */
void swap(int *firstValue, int *secondValue) {
	int tmp;
	tmp = *firstValue;
	*firstValue = *secondValue;
	*secondValue = tmp;
}

/**
 * Synartisi pou ektypwnei ta stoixeia enos pinaka akeraiwn.
 */
void printArray(int *array, int length) {
	int i;
	printf("printArray: Size of array = %d.\n", length);
	for (i = 0; i < length; i++) {
		printf("printArray: array[%d] = %d.\n", i, array[i]);
	}
}
