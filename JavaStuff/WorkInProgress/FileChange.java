import java.nio.file.*;

public class FileChange {
    public static void main(String[] args) {
        Path path = Paths.get("~/Documents/testDir/");
        final boolean pathExists = Files.exists(path, new LinkOption[]{ LinkOption.NOFOLLOW_LINKS});
        if (pathExists){
            System.out.println("it does indeed exist");
        }
    }
}