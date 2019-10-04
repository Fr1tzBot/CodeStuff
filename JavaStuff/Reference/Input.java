import java.util.Scanner;
public class input {
  public static void main(String args[]) {
    System.out.println("Enter your username: ");
    Scanner scanner = new Scanner(System.in);
    String username = scanner.nextLine();
    if((username).equals("thehacker10111")){
      System.out.println("welcome, you");
    } else {
      System.out.println("your username is not valid");
    }
  }
}
