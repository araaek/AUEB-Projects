# ΕΡΓΑΣΙΑ ΙΙ - Client - Server Mean Stack

Το Μέρος Β επεκτείνει το frontend του Μέρους Α με backend υλοποίηση τύπου REST API,
χρησιμοποιώντας Node.js, Express και MongoDB, και client εφαρμογή με Angular (μέσω Vite).

Η εφαρμογή αφορά μια πλατφόρμα μαθημάτων, όπου:
- ο χρήστης μπορεί να δει μία λίστα μαθημάτων
- να φιλτράρει ανά κατηγορία
- να δει λεπτομέρειες κάθε μαθήματος
- να εγγραφεί στην πλατφόρμα
## Απαιτούμενο Λογισμικό
- Node.js και npm: https://nodejs.org/en/download
- MongoDB: https://www.mongodb.com/try/download/community

## Γενική Αρχιτεκτονική

- Client: Angular + Vite
- Server: Node.js + Express
- Database: MongoDB
- Επικοινωνία: REST API (JSON)
- Proxy: Vite proxy /api → http://localhost:PORT

Ροή δεδομένων:
- Ο client φορτώνει τα μαθήματα καλώντας `GET /api/courses` μέσα από το `ApiService`.
- Η σελίδα `/courses` εφαρμόζει φίλτρα (category, level) στον server και ενημερώνει τη λίστα.
- Η σελίδα `/courses/:slug` καλεί `GET /api/courses/:id` για να εμφανίσει λεπτομέρειες,
  μαζί με βιβλία και βίντεο.
- Η φόρμα `/register` συλλέγει στοιχεία φοιτητή, προτιμήσεις μαθημάτων και τα στέλνει
  στον server (endpoint δημιουργίας χρήστη/εγγραφής).
- Τα δεδομένα αποθηκεύονται στη MongoDB μέσω Mongoose, ώστε να είναι διαθέσιμα
  για μελλοντικά αιτήματα.

## REST API – Endpoints

### Μαθήματα

- `GET /api/courses`
  - Παράμετροι query: `category`, `level`, `q` (αναζήτηση κειμένου).
  - Επιστρέφει λίστα μαθημάτων σε μορφή JSON.

- `GET /api/courses/:id`
  - Επιστρέφει πλήρες αντικείμενο μαθήματος:
    τίτλος, κατηγορία, επίπεδο, περιγραφές, εικόνα, βιβλία, βίντεο.

### Χρήστες / Εγγραφές

- `POST /api/users`
  - Δημιουργεί νέο χρήστη/φοιτητή με βασικά στοιχεία (όνομα, email, επίπεδο).

- `POST /api/enrollments`
  - Δημιουργεί εγγραφή φοιτητή σε ένα μάθημα.

- `GET /api/enrollments?userId=...`
  - Επιστρέφει όλες τις εγγραφές ενός χρήστη.

## Υλοποιημένη Λειτουργικότητα

- Πλήρης επικοινωνία client–server
- Φόρτωση μαθημάτων από MongoDB
- Φιλτράρισμα μέσω query parameters
- Καθαρός διαχωρισμός routes / controllers / models
- Κεντρικός χειρισμός σφαλμάτων
- Proxy ώστε ο client να μη γνωρίζει backend URL

## Φάκελοι

- /client → frontend εφαρμογή
- /server → backend REST API
