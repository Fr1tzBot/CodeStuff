import java.util.Scanner;;

public class ForLoop {

    public static void main(String args[]) {
        //ask user to enter their name
        System.out.println("What's Your Name?");
        Scanner scanner = new Scanner(System.in);
        String name = scanner.nextLine();
        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        //iterate through each character in the name
        for (int i = 0; i < name.length(); i++) {
            //print each character's index in the alphabet
            System.out.println(name.charAt(i) + " is at index " + alphabet.indexOf(name.charAt(i)));
        }
    }
}
