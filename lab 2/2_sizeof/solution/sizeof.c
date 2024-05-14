#include <stdio.h>

/**
	Programma pou typwnei ta megethi twn basikwn typwn (p.x. int) se bits. To programma exei kapoia lathi. 
	Tip: H sizeof epistrefei to plithos se bytes.
**/
int main(void) { //isodynamo tou "main(int argc, char** argv)" an den xreiazomaste parametrous
    printf("#bits in a char = %lu \n", sizeof(char) * 8); // x 8 gia na einai to apotelesma se bits
    printf("#bits in a short = %lu \n", sizeof(short) * 8);
    printf("#bits in a int = %lu \n", sizeof(int) * 8);
    printf("#bits in a long = %lu \n", sizeof(long) * 8);
    printf("#bits in a float = %lu \n", sizeof(float) * 8);
    printf("#bits in a double = %lu \n", sizeof(double) * 8);
    printf("#bits in a long double = %lu \n", sizeof(long double) * 8);
    return 0;
}
