import java.util.concurrent.ThreadLocalRandom;
public class exceptions {
       public static int rand (int min, int max){
        int randomNum = ThreadLocalRandom.current().nextInt(min, max + 1);
        return randomNum;
    }
   public static void main(String args[]) {
      try{
        System.out.println("running code to throw exception...");
        int num[] = {1, 2, 3, 4};
        int counter = 0;
        while (counter <= 6) {
            System.out.println("list digit " + num[counter]);
            System.out.println("div out " + counter / rand(0, 2));
            counter = counter + 1;
        }
        
        
      } catch (ArrayIndexOutOfBoundsException e) {
        System.out.println("caught out of range error");
      } catch (ArithmeticException e) {
          System.out.println("caught division by zero error");
      }
   }
}
