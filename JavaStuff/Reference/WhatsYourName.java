import java.util.Scanner;
public class WhatsYourName {
  public static void main(String args[]) {
    System.out.println("What's Your Name?");
    Scanner scanner = new Scanner(System.in);
    String Name = scanner.nextLine();
    System.out.println("Nice to Meet You, " + Name);
    scanner.close();
  }
}
