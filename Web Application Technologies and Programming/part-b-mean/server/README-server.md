# Server – ΕΡΓΑΣΙΑ ΙΙ (MEAN Stack)

## Περιγραφή  
Ο φάκελος `server/` περιέχει το backend της Εργασίας ΙΙ.

Ο server υλοποιείται με **Node.js**, **Express** και **MongoDB** και παρέχει REST API
για τη διαχείριση μαθημάτων (courses).  
Η δομή ακολουθεί την προτεινόμενη αρχιτεκτονική της εκφώνησης

## Εγκατάσταση
Από τον φάκελο `server/`: 

    npm install

## Εκκίνηση server
### Development mode

    npm run dev
### Production mode

    npm start

   
Ο server ξεκινά προεπιλεγμένα στη διεύθυνση: 
`http://localhost:4000`

## MongoDB
Απαιτείται τοπική εγκατάσταση MongoDB.

Η βάση δεδομένων ονομάζεται elearn_db, και ορίζεται από τη μεταβλητή MONGODB_URI (δες το αρχείο `.env.example`).

#### `.env.example`
```
MONGODB_URI=mongodb://localhost:27017/elearn_db
PORT=4000
```

Ο server χρησιμοποιεί αρχείο `.env`.

**Βάζουμε μερικά μαθήματα στην Mongo εκτελώντας το MongoDB Compass (το αρχείο courses.json περιέχει 8 μαθήματα)**


## Σχόλια

Η υλοποίηση ακολουθεί την αρχιτεκτονική REST και διαχωρίζει καθαρά:
- routes
- controllers
- models
- middleware
ώστε να είναι επεκτάσιμη 