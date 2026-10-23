/* 
ΚΟΥΤΣΟΝΙΚΟΛΑΣ ΕΥΣΤΑΘΙΟΣ  p3220093
ΚΟΥΜΠΑΓΙΩΤΗΣ ΕΥΑΓΓΕΛΟΣ   p3220088
*/

// Σταθερές για τον αριθμό των τηλεφωνητών, παρασκευαστών, φούρνων και διανομέων
#define N_TEL 2
#define N_COOK 2
#define N_OVEN 10
#define N_DELIVERER 10

// Χρονικό διάστημα για την εμφάνιση του επόμενου πελάτη
#define T_ORDER_LOW 1
#define T_ORDER_HIGH 5

// Πλήθος πιτσών που μπορεί να παραγγείλει ένας πελάτης
#define N_ORDER_LOW 1
#define N_ORDER_HIGH 5

// Πιθανότητες για τον τύπο κάθε πίτσας
#define P_MARGARITA 0.35
#define P_PEPERONI 0.25
#define P_SPECIAL 0.40

// Χρονικό διάστημα για την χρέωση της πιστωτικής κάρτας του πελάτη
#define T_PAYMENT_LOW 1
#define T_PAYMENT_HIGH 3

// Πιθανότητα αποτυχίας χρέωσης πιστωτικής κάρτας
#define P_FAIL 0.05

// Κόστος κάθε τύπου πίτσας
#define C_MARGARITA 10
#define C_PEPPERONI 11
#define C_SPECIAL 12

// Χρόνος προετοιμασίας κάθε πίτσας από τον παρασκευαστή
#define T_PREP 1

// Χρόνος ψησίματος κάθε πίτσας σε φούρνο
#define T_BAKE 10

// Χρόνος πακεταρίσματος κάθε πίτσας από τον διανομέα
#define T_PACK 1

// Χρονικό διάστημα για την παράδοση της παραγγελίας
#define T_DEL_LOW 5
#define T_DEL_HIGH 15


// structure για να αποθηκεύουμε την παραγγελία του πελάτη
typedef struct customerOrder{
    int pizzas;
    int margarita_pizzas;
	int pepperoni_pizzas;
	int special_pizzas;
} CUSTOMER_ORDER;





