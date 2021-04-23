public class ForLoop {
    public static void main(String args[]) {
        int arrayToIndexThrough[] = { 1, 2, 4, 8, 16, 32, 64, 128 };
        int i;
        //Index through an array
        for (i=0; i<arrayToIndexThrough.length; i++){
            System.out.println(arrayToIndexThrough[i]);
        }
        //Repeat a set number of times (10)
        for (i=1; i<=10; i++){
            System.out.println(i);
        }
    }
}
