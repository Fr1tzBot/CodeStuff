public class WarmupDay2 {
	public static void main(String[] args) {
		int[] a;
		a = new int[3];
		a[0] = 10;
		a[1] = 5;
		a[2] = 7;
		int out = 0;
		int out2 = 9999999;
		for (int i = 0; i < a.length; i++) {
			if (a[i] > out) {
				out = a[i];
			}
			if (a[i] < out2) {
				out2 = a[i];
			}
		}
		System.out.println(out);
		System.out.println(out2);
	}
}
