/*
 * Paradeigma xrisis struct kai typedef. Me ta structs orizoume dikous mas typous dedomenwn. 
 * Me xrisi tis typedef mporoume na dwsoume dika mas onomata stous typous dedomenwn.
 */
#include <stdio.h>

//orismos typou byte
typedef char byte;

//orismos typou bool
typedef int bool;

//orismos tou struct kai xrisi typedef gia allagi tou onomatos
typedef struct telephone {
		char *name;
		int number;
} TELEPHONE;


int main(void){
	TELEPHONE index;

	//ousiastika sizeof(TELEPHONE) = sizeof(char *) + sizeof(int)
	printf("sizeof(TELEPHONE): %lu\n", sizeof(TELEPHONE));
		
	index.name = "Nikos Z";
	index.number = 685;
	printf("Name: %s.\n", index.name);
	printf("Tel: %d.\n", index.number);
	
	TELEPHONE *indexPtr = &index;

	//allagi tou onomatos.
	(*indexPtr).name = "Giwrgos N";
	printf("IndexPtr Name: %s.\n", (*indexPtr).name);
	//deyteros tropos epilogis tou name.
	//printf("IndexPtr Name: %s.\n", indexPtr->name);

	//ti timi exei to index.name?
	printf("Index Name: %s.\n", index.name);
	
	//ektypwsi tis dieythinsis tou pointer
	printf("Address %p.\n", indexPtr);	

	/*proxwra sto xwro tis mnimis kata sizeof(TELEPHONE) bytes*/
	indexPtr++; 
	printf("New address %p.\n", indexPtr);

	//tha treksei??
	printf("IndexPtr Name: %s.\n", (*indexPtr).name);
	
	return 0;
}

// Perissotera paradeigmata: http://www.codingunit.com/c-tutorial-structures-unions-typedef
