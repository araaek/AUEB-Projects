

// JUnit5
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class CalculatorTest {

    private static class EstimatorStub implements Estimator {

        private int estimation;

        public EstimatorStub(int estimation) {
            this.estimation = estimation;
        }

        @Override
        public int estimate(int[] input) {
            return estimation;
        }
    }

    @Test
    public void testNullInput() {
        Calculator calculator = new Calculator();
        Estimator estimator = new EstimatorStub(0);

        int result = calculator.calculate(null, estimator);
        assertEquals(-1, result);
    }

    @Test
    public void testEmptyInput() {
        Calculator calculator = new Calculator();
        Estimator estimator = new EstimatorStub(0);

        int result = calculator.calculate(new int[] {}, estimator);
        assertEquals(-1, result);
    }

    @Test
    public void testEstimatorPositive() {
        Calculator calculator = new Calculator();
        Estimator estimator = new EstimatorStub(1);

        int result = calculator.calculate(new int[] { 1, 2, 3 }, estimator);
        assertEquals(6, result);
    }

    @Test
    public void testEstimatorNonPositive() {
        Calculator calculator = new Calculator();
        Estimator estimator = new EstimatorStub(-1);

        int result = calculator.calculate(new int[] { 1, 2, 3 }, estimator);
        assertEquals(3, result);
    }

}
