

public class Calculator {

	public int calculate(int[] input, Estimator estimator) {
		if (input == null) {
			return -1;
		}
		
		if (input.length == 0) {
			return -1;
		}
		
		int sum = 0;
		for(int i=0; i<input.length;i++) {
			sum += input[i];
		}
		
		if (estimator.estimate(input) > 0) {
			return sum;
		}
		
		return sum / 2;
	}
}
