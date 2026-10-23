import java.io.*;
import java.util.*;

public class ForwardChaining1 {

    public static void main(String[] args) throws IOException {
        // Διαβάζουμε τη βάση γνώσης από αρχείο
        System.out.print("Εισάγετε το όνομα του αρχείου με τη βάση γνώσης: ");
        Scanner scanner = new Scanner(System.in);
        String fileName = scanner.nextLine();
        
        List<String> knowledgeBase = readKnowledgeBase(fileName);
        
        // Διαβάζουμε τον προς απόδειξη τύπο
        System.out.print("Εισάγετε τον προς απόδειξη τύπο: ");
        String query = scanner.nextLine();

        boolean result = forwardChaining(knowledgeBase, query);

        // Εμφανίζουμε το αποτέλεσμα
        if (result) {
            System.out.println("Αληθές");
        } else {
            System.out.println("Ψευδές");
        }
    }

    // Διαβάζει τη βάση γνώσης από το αρχείο
    private static List<String> readKnowledgeBase(String fileName) throws IOException {
        List<String> knowledgeBase = new ArrayList<>();
        BufferedReader reader = new BufferedReader(new FileReader(fileName));
        String line;
        while ((line = reader.readLine()) != null) {
            if (!line.trim().isEmpty()) {
                knowledgeBase.add(line.trim());
            }
        }
        reader.close();
        return knowledgeBase;
    }

    // Εφαρμόζει τη διαδικασία εξαγωγής συμπερασμάτων προς τα εμπρός
    private static boolean forwardChaining(List<String> knowledgeBase, String query) {
        Set<String> inferred = new HashSet<>();
        Queue<String> agenda = new LinkedList<>();
        Map<String, Integer> count = new HashMap<>();

        // Εισαγωγή γεγονότων στην ατζέντα
        for (String clause : knowledgeBase) {
            if (!clause.contains("->")) {
                agenda.add(clause);
                inferred.add(clause);
            }
        }

        // Έλεγχος αν ο προς απόδειξη τύπος είναι ήδη γεγονός
        if (inferred.contains(query)) {
            return true;
        }

        // Υπολογισμός αριθμού προϋποθέσεων για κάθε κανόνα
        for (String clause : knowledgeBase) {
            if (clause.contains("->")) {
                String[] parts = clause.split("->");
                String[] premises = parts[0].split("&");
                count.put(clause, premises.length);
            }
        }

        // Εξαγωγή συμπερασμάτων
        while (!agenda.isEmpty()) {
            // String fact = agenda.poll();
            // System.out.println("Επεξεργασία γεγονότος: " + fact);

            for (String clause : knowledgeBase) {
                if (clause.contains("->")) {
                    String[] parts = clause.split("->");
                    String[] premises = parts[0].split("&");
                    String conclusion = parts[1].trim();

                    boolean allPremisesTrue = true;
                    for (String premise : premises) {
                        if (!inferred.contains(premise.trim())) {
                            allPremisesTrue = false;
                            break;
                        }
                    }

                    if (allPremisesTrue && !inferred.contains(conclusion)) {
                        // System.out.println("Κανόνας πυροδοτήθηκε: " + clause);
                        agenda.add(conclusion);
                        inferred.add(conclusion);

                        if (conclusion.equals(query)) {
                            return true;
                        }
                    }
                }
            }
        }
        return false;
    }
}
