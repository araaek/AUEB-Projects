#include <stdio.h>

/**
	Vreite ta lathi sta parakatw printf statements. Diorthwste ta lathi kai 
	ektypwste to parakatw mhnyma xrisimopoiwntas tis metavlites tou 
	programmatos:
	Hello to the world!
    Today the humidity level is 23%.
**/
int main(void) {
   char c1 = 't';
   char c2 = 'o';
   char str[] = "the world";
   int humidity = 22;
   
   // printf("Hello %d\n", str);  // LA8OS!! GIATI?  
   //Apantisi: To %d xrisimopoieite gia ektypwsi akeraiou. To swsto einai i xrisi %s. Xrhsh %c gia xarakthres.
   
   // printf("Hello %s %d\n", str);  // LA8OS!! GIATI?  
   //Apantisi: To %d den xreiazetai. Grafoyme to keimeno, kai ayxanoume to humidity kata 1
   
   printf("Hello %c%c %s!\n", c1, c2, str);
   printf("Today the humidity level is %d%%.\n", ++humidity);

   return 0;
}
