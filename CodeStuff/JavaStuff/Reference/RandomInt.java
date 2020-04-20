import java.util.concurrent.ThreadLocalRandom;

public class RandomInt {
    public static int rand (int min, int max){
        int randomNum = ThreadLocalRandom.current().nextInt(min, max + 1);
        return randomNum;
    }
    public static void main(String[] args) {
        System.out.println(rand(0, 100));
    }
}
