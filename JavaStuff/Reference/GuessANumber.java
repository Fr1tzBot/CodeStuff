import java.util.concurrent.ThreadLocalRandom;
import java.util.Scanner;
public class guessNumber{
    public static int rand (int min, int max){
        int randomNum = ThreadLocalRandom.current().nextInt(min, max + 1);
        return randomNum;
    }
    public static void main(String args[]) {
        System.out.println("Generating Number...");
        int rando = rand(0, 10);
        String num = String.valueOf(rando);
        boolean stat = true;
        System.out.println("Now, Guess! Number is between 0 and 10");
        Scanner scanner = new Scanner(System.in);
        String guess = "11";
        while (true){
            stat = (!(guess.equals(num)));
            if (stat && !(guess == "11")){
                System.out.println("Try Again");
                guess = scanner.nextLine();
                continue;
            }else{
                if(guess == "11") {
                    guess = scanner.nextLine();
                }else{
                    System.out.println("Correct!");
                    break;
                }
            }
        }
    }
}
