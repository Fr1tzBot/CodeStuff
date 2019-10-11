import java.lang.*;
public class Variable {
	public static void main(String[] args) {
	    String yay;
	    yay = "yay ";
	    int num;
	    num = -10;
	    num = Math.abs(num);
	    num = num * num;
	    num = num / num;
	    num = num + num;
	    num = num - num;
	    System.out.println(yay + num); // should print yay 0
	    if (num == 0) {
		    System.out.println("it works!");
	    }
	}
}
