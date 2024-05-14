#include <stdio.h>

/**
	Na dimiourgisete ena programma to opoio tha
	emfanizei to onoma tou ektelesimou kathws kai ta orismata tou 
	programmatos.
**/		
int main(int argc, char** argv){
    int i = 0;  
    
	//Sti prwti thesi tou pinaka orismatwn argv swzetai to onoma tou ektelesimou.
	printf("Program call:\t\"%s\"\n", argv[0]);
	
	//Diatrexoume ton pinaka argv ektos apo tin prwti thesi gia na typwsoume
	//tis ypoloipes metavlites. To plithos twn metavlitwn mas einai gnwsto
	//mesw tis metavlitis argc.
    for (i=1; i<argc; i++) { 
       printf("argument[%d]:\t%s\n", i, argv[i]);	
    }

    return 0;	
} 
