import java.util.PriorityQueue;

public class aStar {

    private static int counter = -1;
    static boolean counterHelp = false;

    public static State solve(State start, int maxCrossings) {
        PriorityQueue<State> closedList = new PriorityQueue<>();
        PriorityQueue<State> openList = new PriorityQueue<>();

        start.f = start.g + start.evaluate();
        openList.add(start);

        while (!openList.isEmpty() && counter < maxCrossings) {
            State n = openList.peek();
            counter++;
            if (n.isTerminal()) {
                return n;
            }

            for (State child : n.getChildren()) {

                int totalWeight = n.g + 1;

                if (!openList.contains(child) && !closedList.contains(child)) {
                    child.setFather(n);
                    child.g = totalWeight;
                    child.f = child.g + child.evaluate();
                    openList.add(child);
                    counterHelp = true;
                } else {
                    if (totalWeight < child.g) {
                        child.setFather(n);
                        child.g = totalWeight;
                        child.f = child.g + child.evaluate();

                        if (closedList.contains(child)) {
                            closedList.remove(child);
                            openList.add(child);
                            counterHelp = true;
                        }
                    }
                }
            }
            if (!counterHelp) {
                counter--;
            }
            counterHelp = false;
            openList.remove(n);
            closedList.add(n);
        }
        return null;
    }

}
