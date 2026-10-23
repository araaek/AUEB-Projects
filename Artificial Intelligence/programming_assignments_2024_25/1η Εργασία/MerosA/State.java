import java.util.*;

public class State implements Comparable<State> {

    private static int N;
    private static int M;
    private int cannibals;
    private int cannibalsRight;
    private int missionaries;
    private int missionariesRight;
    private char boat;
    private int cost;
    private State father = null;
    int f;
    int g;

    public State(char boat, int N, int M) {
        this.N = N;
        this.M = M;
        this.cannibals = N;
        this.missionaries = N;
        this.boat = boat;
        cannibalsRight = N - cannibals;
        missionariesRight = N - missionaries;
    }

    public State(int cannibals, int missionaries, char boat) {
        this.cannibals = cannibals;
        this.missionaries = missionaries;
        this.boat = boat;
        cannibalsRight = N - cannibals;
        missionariesRight = N - missionaries;
    }

    public State getFather() {
        return father;
    }

    public void setFather(State father) {
        this.father = father;
    }

    public boolean isValid() {
        return missionaries >= 0 && missionaries <= N
                && cannibals >= 0 && cannibals <= N
                && missionariesRight >= 0 && missionariesRight <= N
                && cannibalsRight >= 0 && cannibalsRight <= N
                && (missionaries == 0 || missionaries >= cannibals)
                && (missionariesRight == 0 || missionariesRight >= cannibalsRight)
                && ((boat == 'l' && missionaries + cannibals > 0)
                || (boat == 'r' && missionariesRight + cannibalsRight > 0));
    }

    public ArrayList<State> getChildren() {
        ArrayList<State> children = new ArrayList<>();
        if (boat == 'l') {
            for (int i = 0; i <= M; i++) {
                for (int j = 0; j <= M; j++) {
                    if (i + j > M | (i == 0 && j == 0) | (j < i && j != 0)) {
                        continue;
                    }
                    State temp = new State(cannibals - i, missionaries - j, 'r');

                    if (temp.isValid()) {
                        children.add(temp);
                    }
                }
            }
        } else {
            for (int i = 0; i <= M; i++) {
                for (int j = 0; j <= M; j++) {
                    if (i + j > M | (i == 0 && j == 0) | (j < i && j != 0)) {
                        continue;
                    }
                    State temp = new State(cannibals + i, missionaries + j, 'l');
                    if (temp.isValid()) {
                        children.add(temp);
                    }
                }
            }
        }
        return children;
    }

    public int evaluate() {

        if (boat == 'r' && cannibals + missionaries > 0) {
            cost = 2 * (cannibals + missionaries);
        } else if (boat == 'l' && cannibals + missionaries == 1) {
            cost = 1;
        } else if (boat == 'l' && cannibals + missionaries > 1) {
            cost = 2 * (cannibals + missionaries) - 3;
        } else if (cannibals + missionaries == 0) {
            cost = 0;
        }
        return cost;
    }

    public boolean isTerminal() {
        return cannibals == 0 && missionaries == 0 && boat == 'r';
    }

    @Override
    public String toString() {
        String l = "";
        String r = "";
        String b;
        for (int i = 1; i <= missionaries; i++) {
            l += "M ";
        }
        for (int i = 1; i <= cannibals; i++) {
            l += "C ";
        }
        for (int i = 1; i <= missionariesRight; i++) {
            r += " M";
        }
        for (int i = 1; i <= cannibalsRight; i++) {
            r += " C";
        }
        if (boat == 'l') {
            b = "\\__/                 ";
        } else {
            b = "                 \\__/";
        }
        return l +  b +  r;
    }

    @Override
    public boolean equals(Object obj) {
        if (!(obj instanceof State)) {
            return false;
        }
        State otherState = (State) obj;
        return missionaries == otherState.missionaries
                && cannibals == otherState.cannibals
                && missionariesRight == otherState.missionariesRight
                && cannibalsRight == otherState.cannibalsRight
                && boat == otherState.boat;
    }

    @Override
    public int compareTo(State s) {
        return Double.compare(this.cost, s.cost);
    }

}
