public class main {
    public static void main(String[] args) {
        Tally tally = new Tally();
        tally.increaseCount();
        System.out.println(tally.getCount());
        tally.resetCount();
        System.out.println(tally.getCount());
        tally.decreaseCount();
        System.out.println(tally.getCount());
    }
}
