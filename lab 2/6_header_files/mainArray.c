//aparaitito gia na kanoume include tis synartiseis tou .h
//pou dimiourgisame.
#include "my_functions.h"

/**
 * Main pou xrisimopoiei tin printArray synartisi.
 */
int main(void) {
	int prims_1[] = {2,3,5,7,9,11,13};
	int length = sizeof(prims_1) / sizeof(prims_1[0]);
	printArray(&prims_1[0], length);
	return 0;
}
