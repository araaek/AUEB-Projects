#include <stdio.h>

/**
	Na ftiaksete ena programma pou typwnei ta megethi twn basikwn typwn (p.x. int) se bits. 
	To programma exei kapoia lathi. 
	Tip: H sizeof epistrefei to plithos se bytes.
**/
int main() { //isodynamo tou "main(int argc, char** argv)" dioti den xrisimopoiei parametrous
    printf("#bits in a char = %lu\n", sizeof(char)); 
    printf("#bits in a short = %lu\n", sizeof(short));
    printf("#bits in a int = %lu\n", sizeof(int));
    printf("#bits in a long = %lu\n", sizeof(long));
    printf("#bits in a float = %lu\n", sizeof(float));
    printf("#bits in a double = %lu\n", sizeof(double));
    printf("#bits in a long double = %lu\n", sizeof(long double));
    return 0;
}
