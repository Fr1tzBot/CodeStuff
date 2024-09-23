import java.io.File;
import java.io.FileOutputStream;
import java.util.Scanner;

public class Excersize4 {
    public static void main(String[] args) {

        int numberOfContributions = 0;
        double maxContribution = 0;
        double minContribution = 10000000;
        double averageContribution = 0;
        double totalContributions = 0;
        double inputDataFromFile = 0;

        try {
            File file = new File("input.in");
            FileOutputStream fos = new FileOutputStream(file);
            Scanner scnr = new Scanner(file);

            //write random numbers to file in a while loop
            int i = 0;
            while (i < 100) {
                fos.write((int) (Math.random() * 100));
                i = i + 1;
            }

            while (scnr.hasNextLine()) {
                inputDataFromFile = scnr.nextDouble();
                numberOfContributions++;
                totalContributions += inputDataFromFile;
                if (inputDataFromFile > maxContribution) {
                    maxContribution = inputDataFromFile;
                }
                if (inputDataFromFile < minContribution) {
                    minContribution = inputDataFromFile;
                }
            }
        }
    }
}