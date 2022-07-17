import java.lang.Math;
public class DistanceFunction { 
  public static int dist(int l, int n){
    int dif = (l-n);
    dif = Math.abs(dif);
    return dif;
  }
}
