import java.io.*;
import java.util.*;

public class ForwardChaining2 {

    public static void main(String[] args) throws IOException {
        
        System.out.print("Enter the name of the Knowledge Base file: ");
        Scanner scanner = new Scanner(System.in);
        String kbFile = scanner.nextLine().trim();

        HornKnowledgeBaseFOL knowledgeBase = FOLReader.readFromFileKBHornFOL(kbFile);
      
        System.out.print("Enter your query: ");
        String queryInput = scanner.nextLine().trim();

        LiteralFOL query = FOLReader.analyseInputLiteralFOL(queryInput);

        Unifier result = ForwardChainHornFOL.FOL_ForwardChain(knowledgeBase, query, 100, true);

        if (result != null && !result.isFailure()) {
            if (result.getUnifierMap().isEmpty()) {
                System.out.println("TRUE");
            } else{
                System.out.println("Result: " + result);
            }
        } else {
            System.out.println("FALSE");
        }

        scanner.close();
    }
}

interface Unifiable {
    String getName();
}

abstract class TermFOL implements Unifiable {
    protected String name;
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    @Override public String toString() { return name; }
}

class ConstantFOL extends TermFOL {
    public ConstantFOL(String name) { this.name = name; }
}

class VariableFOL extends TermFOL {
    private String baseName;
    public VariableFOL(String name) { this.baseName = name; this.name = name; }
    public String getBaseName() { return baseName; }
    public void setBaseName(String baseName) { this.baseName = baseName; }
}

class Unifier {
    private HashMap<VariableFOL, TermFOL> unifierMap;
    private boolean failure;

    public Unifier() { unifierMap = new HashMap<>(); failure = false; }
    public Unifier(boolean failure) { unifierMap = new HashMap<>(); this.failure = failure; }
    public boolean isFailure() { return failure; }
    public void setFailure(boolean failure) { this.failure = failure; }
    public HashMap<VariableFOL, TermFOL> getUnifierMap() { return unifierMap; }
    @Override public String toString() {
        if (failure) return "NO";
        StringBuilder sb = new StringBuilder("{");
        unifierMap.forEach((k, v) -> sb.append(k).append("/").append(v).append(", "));
        if (!unifierMap.isEmpty()) sb.setLength(sb.length() - 2);
        sb.append("}");
        return sb.toString();
    }
}

class LiteralFOL {
    private String name;
    private TermFOL[] terms;
    private boolean negation;

    public LiteralFOL(String name, int order, boolean negation) {
        this.name = name;
        this.terms = new TermFOL[order];
        this.negation = negation;
    }

    public String getName() { return name; }
    public TermFOL[] getTerms() { return terms; }
    public boolean isNegation() { return negation; }
    public void setTerms(TermFOL[] terms) { this.terms = terms; }
    @Override public String toString() { return name + Arrays.toString(terms); }
}

class HornClauseFOL {
    private List<LiteralFOL> hypotheses;
    private LiteralFOL result;

    public HornClauseFOL(List<LiteralFOL> hypotheses, LiteralFOL result) {
        this.hypotheses = hypotheses;
        this.result = result;
    }

    public List<LiteralFOL> getHypotheses() { return hypotheses; }
    public LiteralFOL getResult() { return result; }
}

class HornKnowledgeBaseFOL {
    private List<HornClauseFOL> clauses = new ArrayList<>();
    public List<HornClauseFOL> getHornClauses() { return clauses; }
}

class FOLReader {
    public static HornKnowledgeBaseFOL readFromFileKBHornFOL(String filename) {
        HornKnowledgeBaseFOL kb = new HornKnowledgeBaseFOL();
        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = br.readLine()) != null) {
                HornClauseFOL clause = parseHornClause(line);
                kb.getHornClauses().add(clause);
            }
        } catch (IOException e) {
            System.err.println("Error reading file: " + e.getMessage());
        }
        return kb;
    }

    public static HornClauseFOL parseHornClause(String input) {
        String[] parts = input.split("=>");
        List<LiteralFOL> hypotheses = new ArrayList<>();
        for (String hyp : parts[0].split("AND")) {
            hypotheses.add(parseLiteral(hyp.trim()));
        }
        LiteralFOL result = (parts.length > 1) ? parseLiteral(parts[1].trim()) : null;
        return new HornClauseFOL(hypotheses, result);
    }

    public static LiteralFOL parseLiteral(String input) {
        int parenIndex = input.indexOf('(');
        String name = input.substring(0, parenIndex);
        String[] termStrings = input.substring(parenIndex + 1, input.length() - 1).split(",");
        TermFOL[] terms = Arrays.stream(termStrings).map(ConstantFOL::new).toArray(TermFOL[]::new);
        return new LiteralFOL(name, terms.length, false);
    }

    public static LiteralFOL analyseInputLiteralFOL(String input) {
        return parseLiteral(input);
    }
}

class ForwardChainHornFOL {
    public static Unifier FOL_ForwardChain(HornKnowledgeBaseFOL kb, LiteralFOL query, int maxSteps, boolean returnFirst) {
        for (HornClauseFOL clause : kb.getHornClauses()) {
            if (clause.getResult() != null && query.getName().equals(clause.getResult().getName())) {
                return new Unifier(); // Placeholder logic
            }
        }
        return new Unifier(true);
    }
}
