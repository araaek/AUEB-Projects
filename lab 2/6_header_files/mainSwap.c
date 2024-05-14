//aparaitito gia na kanoume include tis synartiseis tou .h
//pou dimiourgisame.
#include "my_functions.h"

/**
 * Main pou xrisimopoiei tin swap synartisi.
 */
int main(void) {

	int firstValue = 5, secondValue = 6;
	printf("First value = %d, second value = %d\n", firstValue, secondValue);
	swap(&firstValue, &secondValue);
	printf("First value = %d, second value = %d\n", firstValue, secondValue);

	return 0;
}
