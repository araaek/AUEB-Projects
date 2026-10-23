

#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "p3220088-p3220093-pizza.h"

// Δήλωσεις mutexes
pthread_mutex_t output_mutex, stats_mutex, transaction_mutex;
pthread_mutex_t cook_priority_mutex, oven_priority_mutex, deliverer_priority_mutex;
pthread_mutex_t available_telephoners_mutex, available_cooks_mutex, available_ovens_mutex, available_deliverers_mutex;

// Δηλώσεις μεταβλητών συνθήκης
pthread_cond_t cook_priority_cond, oven_priority_cond, deliverer_priority_cond;
pthread_cond_t available_telephoners_cond, available_cooks_cond, available_ovens_cond, available_deliverers_cond;

int init_seed;
int failed_transactions = 0;
int succesful_transactions = 0;
int total_margarita = 0;
int total_pepperoni = 0;
int total_special = 0;
int income = 0;

int available_telephoners = N_TEL;
int available_cooks = N_COOK;
int available_ovens = N_OVEN;
int available_deliverers = N_DELIVERER;

int priority = 1;
int cook_priority = 1;
int oven_priority = 1;
int packer_priority = 1;
int deliverer_priority = 1;

double max_order_time = 0;
double max_cooling_time = 0;
double sum_order_time = 0;
double sum_cooling_time = 0;

// Αρχικοποίηση mutex
void initialize_mutex(pthread_mutex_t *mutex){
	int rc = pthread_mutex_init(mutex, NULL);
    if (rc != 0){
        printf("ERROR: return code from pthread_mutex_init() is %d\n", rc);
        exit(-1);
    }
}

// Αρχικοποίηση condition
void initialize_condition(pthread_cond_t *cond){
	int rc = pthread_cond_init(cond, NULL);
    if (rc != 0) {
    	printf("ERROR: return code from pthread_cond_init() is %d\n", rc);
       	exit(-1);
    }
}

// Κλείδωμα του mutex
void lock_mutex(pthread_mutex_t *mutex, void* t){
	int rc = pthread_mutex_lock(mutex);
    if (rc != 0) {	
		printf("ERROR: return code from pthread_mutex_lock() is %d\n", rc);
		pthread_exit(t);
	}
}

// Ξεκλείδωμα του mutex
void unlock_mutex(pthread_mutex_t *mutex, void* t){
	int rc = pthread_mutex_unlock(mutex);
    if (rc != 0){
        printf("ERROR: return code from pthread_mutex_unlock() is %d\n", rc);
		pthread_exit(t);
    }
}

// Καταστροφή mutex
void destroy_mutex(pthread_mutex_t *mutex){
    int rc = pthread_mutex_destroy(mutex);
	if (rc != 0){
        printf("ERROR: return code from pthread_mutex_destroy() is %d\n", rc);
		exit(-1);
    } 
}

// Καταστροφή condition
void destroy_condition(pthread_cond_t *cond){
	int rc = pthread_cond_destroy(cond);
    if (rc != 0){
        printf("ERROR: return code from pthread_cond_destroy() is %d\n", rc);
		exit (-1);
    } 
}

// Επιστρέφει έναν τυχαίο ακέραιο μεταξύ του min και του max (συμπεριλαμβανομένων)
int generateRandomNumber(int min, int max, unsigned int * seed){
    return ((rand_r(seed))%(max-min+1))+min;
}
	

// Επιστρέφει το είδος της πίτσας λαμβάνοντας υπόψη τις πιθανότητες
// 1 για Μαργαρίτα, 2 για πεπερόνι, 3 για σπέσιαλ
int generateRandomPizzaCode(unsigned int *seed, float Pm, float Pp, float Ps) {
    // Δημιουργία τυχαίου αριθμού 0..1
    float randomProbability = (float)rand_r(seed) / RAND_MAX;

    if (randomProbability < Pm) {
        return 1; // Μαργαρίτα
    } else if (randomProbability < Pm + Pp) {
        return 2; // Πεπερόνι
    } else {
        return 3; // Σπέσιαλ
    }
}

// Επιστρέφει 1 με πιθανότητα p και 0 με πιθανότητα 1-p.
int checkOrderFailure(float p, unsigned int *seed){
    double uni = (double) rand_r(seed) / RAND_MAX;

    if (uni < p) return 1;
    return 0;
}


// Διαδικασία παραγγελίας
void *order_service_procedure(void *t){

    struct timespec start_time, finished_baking_time, timeFinishedPacking, delivered_time; 
    int order_priority, wait;
    int* oid = (int *) t; 
    CUSTOMER_ORDER order;

    // seed για κάθε thread
    unsigned int seed = init_seed + *oid;

    // ΔΕΣΜΕΥΣΗ ΤΗΛΕΦΩΝΗΤΗ, ΠΑΡΑΓΓΕΛΙΑ ΠΙΤΣΩΝ ΚΑΙ ΠΛΗΡΩΜΗ

	// Τώρα απασχόλησε ένα τηλεφωνητή
	lock_mutex(&available_telephoners_mutex, t);
	while(available_telephoners == 0){
		pthread_cond_wait(&available_telephoners_cond, &available_telephoners_mutex);
	}
	available_telephoners -= 1;
	unlock_mutex(&available_telephoners_mutex, t);
	
    // Κρατάμε την στιγμή έναρξης της παραγγελίας
    clock_gettime(CLOCK_REALTIME, &start_time);

	
	// Συνολικός αριθμός πιτσών
    order.pizzas = generateRandomNumber(N_ORDER_LOW, N_ORDER_HIGH, &seed);

    order.margarita_pizzas = 0;
    order.pepperoni_pizzas = 0;
	order.special_pizzas = 0;
	
    // Υπολογισμός του τύπου κάθε πίτσας
    int i,type;
    for (i = 0; i < order.pizzas; i++){
		type = generateRandomPizzaCode(&seed, P_MARGARITA, P_PEPERONI, P_SPECIAL);
        if (type == 1){
            order.margarita_pizzas++;
		} else if (type == 2){
			order.pepperoni_pizzas++;
        } else{
			order.special_pizzas++;
		}
	}
    
    // Υπολογισμός χρόνου για χρέωση της πιστωτικής κάρτας
    wait = generateRandomNumber(T_PAYMENT_LOW, T_PAYMENT_HIGH, &seed);
	sleep(wait);

    // Κλείδωμα για την ενημέρωση της συναλλαγής
    lock_mutex(&transaction_mutex, t);
    
    // Κλείδωμα για εμφάνιση στην οθόνη
    lock_mutex(&output_mutex, t);

    // Με πιθανότητα P_FAIL η συναλλαγή αποτυγχάνει
    if (checkOrderFailure(P_FAIL, &seed)){
        printf("Order number %d failed\n", *oid);
        failed_transactions += 1;

        // Ξεκλείδωμα ενημέρωσης συναλλαγής
        unlock_mutex(&transaction_mutex, t);
        
        // Ξεκλείδωμα εμφάνισης στην οθόνη
        unlock_mutex(&output_mutex, t);
		
		// Τώρα απελευθέρωσε ένα τηλεφωνητή    
        lock_mutex(&available_telephoners_mutex, t);
        available_telephoners += 1;
        unlock_mutex(&available_telephoners_mutex, t); 
        // Τερματισμός thread και αποδεύσμευση πόρων
        pthread_exit(NULL);

    } else {
        printf("Order number %d succesful\n", *oid);

        // Ξεκλείδωμα εμφάνισης στην οθόνη
        unlock_mutex(&output_mutex, t);

        total_margarita += order.margarita_pizzas;
        total_pepperoni += order.pepperoni_pizzas;
		total_special += order.special_pizzas;
		
		income += C_MARGARITA * order.margarita_pizzas + C_PEPPERONI * order.pepperoni_pizzas + C_SPECIAL * order.special_pizzas;
        succesful_transactions += 1;

        // Ξεκλείδωμα ενημέρωσης συναλλαγής
        unlock_mutex(&transaction_mutex, t);

        order_priority = priority++; 
	}
    // Τώρα απελευθέρωσε ένα τηλεφωνητή    
    lock_mutex(&available_telephoners_mutex, t);
    available_telephoners += 1;
    unlock_mutex(&available_telephoners_mutex, t);
    pthread_cond_signal(&available_telephoners_cond);
    // ΤΕΛΟΣ ΔΕΣΜΕΥΣΗ ΤΗΛΕΦΩΝΗΤΗ, ΠΑΡΑΓΓΕΛΙΑ ΠΙΤΣΩΝ ΚΑΙ ΠΛΗΡΩΜΗ


    // ΔΕΣΜΕΥΣΗ ΠΑΡΑΣΚΕΥΑΣΤΗ
    lock_mutex(&cook_priority_mutex, t);
    while(cook_priority != order_priority){
        pthread_cond_wait(&cook_priority_cond, &cook_priority_mutex);
    }
    
    lock_mutex(&available_cooks_mutex, t);

    while(available_cooks == 0){
        pthread_cond_wait(&available_cooks_cond, &available_cooks_mutex);
    }
    available_cooks -= 1;
    unlock_mutex(&available_cooks_mutex, t);
    cook_priority += 1;
    unlock_mutex(&cook_priority_mutex, t);
    pthread_cond_broadcast(&cook_priority_cond); 

    // Χρόνος παρασκευής παραγγελίας
    sleep(T_PREP * order.pizzas);

    
	// ΔΕΣΜΕΥΣΗ ΦΟΥΡΝΩΝ
    lock_mutex(&oven_priority_mutex, t);
    while(order_priority != oven_priority){
        pthread_cond_wait(&oven_priority_cond, &oven_priority_mutex);
    }

    // Κάθε φούρνος χωράει μία πίτσα
    lock_mutex(&available_ovens_mutex, t);

    // Αναμονή για διαθέσιμους φούρνους
    while(available_ovens < order.pizzas){
        pthread_cond_wait(&available_ovens_cond, &available_ovens_mutex);
    }
    available_ovens -= order.pizzas;
    unlock_mutex(&available_ovens_mutex, t);

    oven_priority += 1;
    unlock_mutex(&oven_priority_mutex, t);
    pthread_cond_broadcast(&oven_priority_cond); 
    
    
	// ΑΠΟΔΕΣΜΕΥΣΗ ΠΑΡΑΣΚΕΥΑΣΤΗ
    lock_mutex(&available_cooks_mutex, t);
    available_cooks += 1;
    unlock_mutex(&available_cooks_mutex, t);
    pthread_cond_signal(&available_cooks_cond); 

    // Χρόνος ψησίματος
    sleep(T_BAKE);

    // Κρατάμε τον χρόνο που ολοκληρώθηκε το ψήσιμο
    clock_gettime(CLOCK_REALTIME, &finished_baking_time);

    // ΤΟ ΨΗΣΙΜΟ ΟΛΟΚΛΗΡΩΘΗΚΕ

    // ΔΕΣΜΕΥΣΗ ΔΙΑΝΟΜΕΑ
    lock_mutex(&deliverer_priority_mutex, t);
    while(order_priority != deliverer_priority){
        pthread_cond_wait(&deliverer_priority_cond, &deliverer_priority_mutex); 
    }

    lock_mutex(&available_deliverers_mutex, t);
    while (available_deliverers == 0){
        pthread_cond_wait(&available_deliverers_cond, &available_deliverers_mutex);
    }
    available_deliverers -= 1;
    unlock_mutex(&available_deliverers_mutex, t);
    deliverer_priority += 1;
    unlock_mutex(&deliverer_priority_mutex, t);
    pthread_cond_broadcast(&deliverer_priority_cond);
	
    // Χρόνος πακεταρίσματος
    sleep(T_PACK * order.pizzas);
    
    // Κρατάμε την στιγμή που ολοκληρώθηκε το πακετάρισμα
    clock_gettime(CLOCK_REALTIME, &timeFinishedPacking);

    // ΑΠΟΔΕΣΜΕΥΣΗ ΦΟΥΡΝΩΝ
    lock_mutex(&available_ovens_mutex, t);
    available_ovens += order.pizzas;
    unlock_mutex(&available_ovens_mutex, t);
    pthread_cond_signal(&available_ovens_cond); 

    // Εκτύπωση του χρόνου ετοιμασίας της παραγγελίας
	double orderPreparationTime = timeFinishedPacking.tv_sec - start_time.tv_sec;
    lock_mutex(&output_mutex, t);
    printf("Order number %d prepared in %.0f minutes\n", *oid, orderPreparationTime);
    unlock_mutex(&output_mutex, t);

    // Υπολογισμός χρόνου για την παράδοση της παραγγελίας
	wait = generateRandomNumber(T_DEL_LOW, T_DEL_HIGH, &seed);
    sleep(wait);
    
    // Κρατάμε την στιγμή που παραδόθηκε η παραγγελία
    clock_gettime(CLOCK_REALTIME, &delivered_time);

    // Εκτύπωση του χρόνου παράδοσης της παραγγελίας
    double order_time = delivered_time.tv_sec - start_time.tv_sec;
    lock_mutex(&output_mutex, t);
    printf("Order number %d delivered in %.0f minutes\n", *oid, order_time);
    unlock_mutex(&output_mutex, t);

    // Ο χρόνος που απαιτείται για να επιστρέψει ο διανομέας
	// είναι ο ίδιος που χρειάζεται για να πάει
    sleep(wait);

    // Αποδέσμευση διανομέα
    lock_mutex(&available_deliverers_mutex, t);
    available_deliverers += 1;
    unlock_mutex(&available_deliverers_mutex, t);
    pthread_cond_signal(&available_deliverers_cond); 
	// Ο ΔΙΑΝΟΜΕΑΣ ΕΠΕΣΤΡΕΨΕ

    // Υπολογισμός χρόνου κρυώματος
	// από την στιγμή που βγαίνουν οι πίτσες απο τον φούρνο μέχρι να παραδοθούν
    double cooling_time = delivered_time.tv_sec - finished_baking_time.tv_sec;
    
    lock_mutex(&stats_mutex, t);

    // Εύρεση του μέγιστου χρόνου εξυπηρέτησης 
	// και του μέγιστου χρόνου κρυώματος
    if (order_time > max_order_time) max_order_time = order_time;
    if (cooling_time > max_cooling_time) max_cooling_time = cooling_time;

    // Υπολογισμός αθροισμάτων
    sum_order_time += order_time;
    sum_cooling_time += cooling_time;

    unlock_mutex(&stats_mutex, t);
    pthread_exit(t);
}

int main(int argc, char* argv[]){

    int rc, N_cust;
	pthread_t *threads;

    // Αρχικοποίηση mutexes
    initialize_mutex(&output_mutex);
    initialize_mutex(&transaction_mutex);
    initialize_mutex(&cook_priority_mutex);
    initialize_mutex(&oven_priority_mutex);
    initialize_mutex(&deliverer_priority_mutex);
	initialize_mutex(&available_telephoners_mutex);
    initialize_mutex(&available_cooks_mutex);
    initialize_mutex(&available_ovens_mutex);
    initialize_mutex(&available_deliverers_mutex);
    initialize_mutex(&stats_mutex);

    // Αρχικοποίηση conditions
	initialize_condition(&cook_priority_cond);
    initialize_condition(&oven_priority_cond);
    initialize_condition(&deliverer_priority_cond);
	initialize_condition(&available_telephoners_cond);
    initialize_condition(&available_cooks_cond);
    initialize_condition(&available_ovens_cond);
    initialize_condition(&available_deliverers_cond);
    
    // Έλεγχος ορθότητας των ορισμάτων της γραμμής εντολών
    if (argc != 3) {
        printf("Usage: %s <Ncust> <Seed>\n", argv[0]);
        exit(-1);
    }

    N_cust = atoi(argv[1]);
    init_seed = atoi(argv[2]);

    if (N_cust <= 0){
        printf("The number of customers must be positive\n");
        exit(-1);
    }
    
    // Δέσμευση μνήμης για τον πίνακα των threads
    threads = (pthread_t *) malloc(N_cust * sizeof(pthread_t));
    if (threads == NULL){
        printf("Not enough memory!\n");
        exit(-1);
    }
    
	unsigned int seed = init_seed;
    int i;
	// ο πρώτος πελάτης δεν περιμένει καθόλου
    int wait = 0; 
    int oids[N_cust];

	// Δημιουργία threads.
    for (i = 0; i < N_cust; i++){
        oids[i] = i + 1;
        rc = pthread_create(&threads[i], NULL, &order_service_procedure, &oids[i]);
        if (rc != 0) {
            printf("ERROR: return code from pthread_create() is %d\n", rc);
            exit(-1);
        }

        // Υπολογισμός χρόνου εμφάνισης του επόμενου πελάτη
		wait = generateRandomNumber(T_ORDER_LOW, T_ORDER_HIGH, &seed);
		sleep(wait);
    }

    // Αναμονή για τερματισμό των threads
    for (i = 0; i < N_cust; i++){
		rc = pthread_join(threads[i], NULL);
        if (rc != 0){
            printf("ERROR: return code from pthread_join() is %d\n", rc);
			exit (-1);
        }
    }
	
	// Εκτυπώσεις συγκεντρωτικών στοιχείων
    if (succesful_transactions > 0){
        printf("Total income: %d\n", income);
		printf("Total margaritas sold: %d\n", total_margarita);
        printf("Total pepperonies sold %d\n", total_pepperoni);
		printf("Total specials sold: %d\n", total_special);
        printf("Succesful transactions: %d\n", succesful_transactions);
        printf("Failed transactions: %d\n", failed_transactions);
		printf("Mean order completion time: %.2f minutes\n", sum_order_time / succesful_transactions);
        printf("Max order completion time: %.2f minutes\n", max_order_time);
        printf("Mean cooling time: %.2f minutes\n", sum_cooling_time / succesful_transactions);
        printf("Max cooling time: %.2f minutes\n", max_cooling_time);
    }else{
        printf("No succesful transactions\n");
    }
    
    // Καταστροφή conditions
    destroy_condition(&cook_priority_cond);
    destroy_condition(&oven_priority_cond);
    destroy_condition(&deliverer_priority_cond);
	destroy_condition(&available_telephoners_cond);
    destroy_condition(&available_cooks_cond);
    destroy_condition(&available_ovens_cond);
    destroy_condition(&available_deliverers_cond);
	
	// Καταστροφή mutexes
    destroy_mutex(&output_mutex);
    destroy_mutex(&transaction_mutex);
    destroy_mutex(&cook_priority_mutex);
    destroy_mutex(&oven_priority_mutex);
    destroy_mutex(&deliverer_priority_mutex);
	destroy_mutex(&available_telephoners_mutex);
    destroy_mutex(&available_cooks_mutex);
    destroy_mutex(&available_ovens_mutex);
    destroy_mutex(&available_deliverers_mutex);
    destroy_mutex(&stats_mutex);
			
    // Απελευθέρωση μνήμης
    free(threads);
	
    return 1;
}