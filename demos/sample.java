/**
 * Class level comment example.
 */
@Component
public class Accumulator {

  private double sum;

  /**
   * Method level comment example.
   *
   * @param sum0 The sum parameter
   */
  public Accumulator(double sum0) {
    sum = sum0;
  }

  public double call(double n) {
    return sum += n;
  }

  public static void main(String[] args) {
    Accumulator localVariable = new Accumulator(1);
    localVariable.call(5);

    String localString = "example of a string \n\t" + args[0];

    System.out.println(new Accumulator(3));
    System.out.println(x.call(2.3));

    Boolean booleanFlag = true;
  }
}
