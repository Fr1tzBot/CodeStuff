public class Tally {
    int count;

    public Tally() {
        count = 0;
    }

    public Tally(int count) {
        this.count = count;
    }

    public void increaseCount() {
        count++;
    }

    public void decreaseCount() {
        count--;
    }

    public int getCount() {
        return count;
    }

    public void resetCount() {
        count = 0;
    }
}

