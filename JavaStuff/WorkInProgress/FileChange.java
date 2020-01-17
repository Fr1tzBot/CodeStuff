import java.io.IOException;
import java.nio.file.*;

public class FileChange {
    public static void main(String[] args) {
        Path dirPath = Paths.get("/home/fritz/Documents/testDir/");
        Path filePath = Paths.get("/home/fritz/Documents/testDir/yeet.txt");
        final boolean pathExists = Files.exists(filePath, new LinkOption[]{ LinkOption.NOFOLLOW_LINKS});
        if (pathExists){
            System.out.println("it does indeed exist");

            try {
                Path newDir = Files.createDirectory(dirPath);
            } 
            catch(FileAlreadyExistsException e){
                System.out.println("The directory Already Exists");
            } 
            catch (IOException e) {
                //something else went wrong
                e.printStackTrace();
            }
        }
        else {
            System.out.println("It does not exist");
        }
    }
}