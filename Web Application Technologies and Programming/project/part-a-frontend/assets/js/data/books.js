const BOOKS = {
    java: [
        {
            title: 'Java Προγραμματισμός, H. M. Deitel, P. J. Deitel, 10η έκδοση, Εκδόσεις Γκιούρδας, 2015.',
            url: 'https://www.mgiurdas.gr/biblia/java-programmatismos-10i-ekdosi'
        },
        {
            title: 'Πλήρες Εγχειρίδιο της Java 7, R. Cadenhead, 6η έκδοση, Εκδόσεις Γκιούρδας, 2013.',
            url: 'https://www.mgiurdas.gr/biblia/plires-egheiridio-tis-java-7-6i-ekdosi'
        },
        {
            title: 'Η Τέχνη και Επιστήμη της Java, E. S. Roberts, Εκδόσεις Κλειδάριθμος, 2008.',
            url: 'https://www.klidarithmos.gr/h-texnh-kai-h-episthmh-ths-java/'
        }
    ],

    python_intro: [
        {
            title: 'Υπολογισμοί και Προγραμματισμός με την Python, John V. Guttag, Εκδόσεις Κλειδάριθμος, 2015.',
            url: 'https://www.klidarithmos.gr/ypologismoi-kai-programmatismos-me-thn-python/'
        },
        {
            title: 'Εισαγωγή στον Προγραμματισμό με την Python, David Schneider, Εκδόσεις Μ. Γκιούρδας, 2016.',
            url: 'https://www.mgiurdas.gr/biblia/eisagogi-ston-programmatismo-me-tin-python'
        },
        {
            title: 'Εισαγωγή στον Προγραμματισμό με την Python, Ν. Α. Αγγελιδάκης, 2015.',
            url: 'https://www.openbook.gr/eisagwgi-ston-programmatismo-me-python/'
        },
        {
            title: 'Εισαγωγή στον Προγραμματισμό με αρωγό τη γλώσσα Python, Γ. Μανής, Εκδόσεις Κάλλιπος, 2015.',
            url: 'https://repository.kallipos.gr/handle/11419/2745'
        },
        {
            title: 'Composing Programs, John DeNero, 2015.',
            url: 'https://www.composingprograms.com/'
        }
    ],

    cpp: [
        {
            title: 'C++ Προγραμματισμός, H. M. Deitel, P. J. Deitel, 9η έκδοση, Εκδόσεις Μ. Γκιούρδας, 2015.',
            url: 'https://www.mgiurdas.gr/biblia/c-programmatismos-9i-ekdosi'
        },

        {
            title: 'Πλήρες Εγχειρίδιο της C++, J. Liberty, B. Jones, 7η έκδοση, Εκδόσεις Μ. Γκιούρδας, 2015.',
            url: 'https://www.mgiurdas.gr/biblia/plires-egheiridio-tis-c-7i-ekdosi'
        },
        {
            title: 'Μάθετε τη C++ από το Μηδέν, H. Schildt, Κλειδάριθμος, 2004.',
            url: 'https://www.klidarithmos.gr/ma8ete-th-c-apo-to-mhden/'
        },
        {
            title: 'C++ Βήμα προς Βήμα, H. Schildt, 2η έκδοση, Εκδόσεις Μ. Γκιούρδας, 2005.',
            url: 'https://www.mgiurdas.gr/biblia/c-vima-pros-vima-0'
        }
    ],

    computer_networks: [
        {
            title: 'Δίκτυα Υπολογιστών, A. S. Tanenbaum, D. J. Wetherall, 5η έκδοση, Εκδόσεις Κλειδάριθμος, 2012.',
            url: 'https://www.klidarithmos.gr/diktya-ypologistwn-5h-amerikanikh-ekdosh/'
        },
        {
            title: 'Δίκτυα Υπολογιστών – Προσέγγιση από πάνω προς τα κάτω, Β. A. Forouzan, F. Mosharraf, Εκδόσεις Παπασωτηρίου, 2012.',
            url: 'https://ekdoseis-papasotiriou.gr/products/9789604910182-forouzan-behrouz-diktua-upologiston'
        },
        {
            title: 'Δίκτυα Υπολογιστών – Μία προσέγγιση από την πλευρά των συστημάτων, L. Peterson, B. Davie, Εκδόσεις Κλειδάριθμος, 2009.',
            url: 'https://www.klidarithmos.gr/diktya-ypologistwn-mia-proseggish-apo-th-skopia-twn-systhmatwn/'
        }
    ],

    communication_networks: [
        {
            title: 'Δίκτυα Υπολογιστών, A. S. Tanenbaum, D. Wetherall, 5η έκδοση, Εκδόσεις Κλειδάριθμος, 2011.',
            url: 'https://www.klidarithmos.gr/diktya-ypologistwn-5h-amerikanikh-ekdosh/'
        },
        {
            title: 'Δίκτυα και Διαδίκτυα Υπολογιστών και Εφαρμογές τους στο Internet, D. Comer, 6η έκδοση, Εκδόσεις Κλειδάριθμος, 2014.',
            url: 'https://www.klidarithmos.gr/diktia-kai-diadiktia-ypologistwn-6h-ekdosh/'
        },
        {
            title: 'Δικτύωση Υπολογιστών – Προσέγγιση από πάνω προς τα κάτω, J. Kurose, K. Ross, 6η έκδοση, Εκδόσεις Γκιούρδας, 2013.',
            url: 'https://www.mgiurdas.gr/biblia/diktyosi-ypologiston-6i-ekdosi'
        },
        {
            title: 'Επικοινωνίες Υπολογιστών και Δεδομένων, W. Stallings, Εκδόσεις Τζιόλα, 2011.',
            url: 'https://www.tziola.gr/book/epikinonies-ypologiston-dedomenon-10i-ekdosi/'
        },
        {
            title: 'Δίκτυα Υπολογιστών – Μία προσέγγιση από την πλευρά των συστημάτων, L. Peterson, B. Davie, Εκδόσεις Κλειδάριθμος, 2009.',
            url: 'https://www.klidarithmos.gr/diktya-ypologistwn-mia-proseggish-apo-th-skopia-twn-systhmatwn/'
        }
    ],

    network_security: [
        {
            title: 'Δίκτυα Υπολογιστών, A. S. Tanenbaum, D. J. Wetherall, 5η έκδοση, Εκδόσεις Κλειδάριθμος, 2012.',
            url: 'https://www.klidarithmos.gr/diktya-ypologistwn-5h-amerikanikh-ekdosh/'
        },
        {
            title: 'Δικτύωση Υπολογιστών – Προσέγγιση από πάνω προς τα κάτω, J. Kurose, K. Ross, 6η έκδοση, Εκδόσεις Γκιούρδας, 2013.',
            url: 'https://www.mgiurdas.gr/biblia/diktyosi-ypologiston-6i-ekdosi/'
        },
        {
            title: 'Επικοινωνίες Υπολογιστών και Δεδομένων, W. Stallings, Εκδόσεις Τζιόλα, 2011.',
            url: 'https://www.tziola.gr/book/epikinonies-ypologiston-dedomenon-10i-ekdosi/'
        }
    ],

    cyber_security: [
        {
            title: 'Πληροφοριακά Συστήματα: Σύγχρονη Ανάλυση & Σχεδίαση, J. Hoffer, J. George, J. Valacich, 6η έκδοση, Εκδόσεις Τζιόλα, 2014.',
            url: 'https://www.tziola.gr/book/plirof/'
        },
        {
            title: 'Μεθοδολογίες Ανάλυσης και Σχεδιασμού Πληροφοριακών Συστημάτων, Ε. Κιουντούζη, 3η έκδοση, Εκδόσεις Ε. Μπένου, 2009.',
            url: 'https://www.protoporia.gr/kiountouzis-euaggelos-methodologies-analusis-kai-sxediasmou-pliroforiakon-sustimaton-83631.html'
        },
        {
            title: 'Requirements Analysis and System Design, L. A. Maciaszek, 3rd ed., Pearson, 2007.',
            url: 'https://www.amazon.com/Requirements-Analysis-Systems-Design-3rd/dp/0321440366'
        },
        {
            title: 'Requirements Engineering: From System Goals to UML Models to Software Specifications, A. van Lamsweerde, Wiley, 2009.',
            url: 'https://www.amazon.com/Requirements-Engineering-System-Software-Specifications/dp/0470012706'
        }
    ],

    databases: [
        {
            title: 'Βάσεις Δεδομένων: Θεωρία και Πράξη, Ε. Ι. Γιαννακουδάκης, Εκδόσεις Μπένος, 2014.',
            url: 'https://www.protoporia.gr/giannakoudakis-emmanouil-i.-vaseis-dedomenon-406650.html'
        },

        {
            title: 'Συστήματα Βάσεων Δεδομένων, Ε. Ι. Γιαννακουδάκης, Εκδόσεις Μπένος, 2009.',
            url: 'https://www.protoporia.gr/giannakoudakis-emmanouil-i.-sustimata-vaseon-dedomenon-sql-84716.html'
        },
        {
            title: 'Σχεδιασμός και Διαχείριση Βάσεων Δεδομένων, Ε. Ι. Γιαννακουδάκης, Εκδόσεις Μπένος, 2009.',
            url: 'https://www.protoporia.gr/giannakoudakis-emmanouil-i.-sxediasmos-kai-diaxeirisi-vaseon-dedomenon-84719.html'
        }
    ]
};

window.BOOKS = BOOKS;
