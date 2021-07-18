import java.util.HashMap;
import java.util.Random;
public class shittyTextRenderer {
    final String startColor;
    final String character;
    final HashMap<String, String> colors;
    private String[][] screen;

    //Hardcoded for now, will fix later(tm)
    public int getRows() { 
        //return Integer.parseInt(System.getProperty("LINES")); 
        return 56;
    }
    public int getCols() { 
        //return Integer.parseInt(System.getProperty("COLUMNS")); 
        return 192;
    }

    public void setFullScreen(String color) {
        int cols = this.getCols();
        int rows = this.getRows();
        String[][] screen = new String[rows][cols];

        int i;
        int j;
        //add colors to all of the sub lists
        for (i=0; i<rows; i++){
            for (j=0; j<cols; j++){
                screen[i][j] = color;
            }
        }
        this.screen = screen;
    }

    public void setColor(int x, int y, String color) { this.screen[y][x] = color; }

    public void display() {
        HashMap<String, String> colors = this.colors;
        String[][] screen = this.screen;

        int cols = this.getCols();
        int rows = this.getRows();
        
        String out = "";
        int i;
        int j;
        for (i=0; i<rows; i++){
            for (j=0; j<cols; j++){
                out += colors.get(screen[i][j]);
            }
            out += "\n";
        }
        System.out.print(out);
    }

    public shittyTextRenderer(String startColor, String character) {
        this.character = character;
        this.startColor = startColor;
        this.colors = new HashMap<String, String>();
        //Attempt to emulate a python dict
        this.colors.put("black",          "\033[30m" + character + "\033[39m");
        this.colors.put("red",            "\033[31m" + character + "\033[39m");
        this.colors.put("red",            "\033[31m" + character + "\033[39m");
        this.colors.put("green",          "\033[32m" + character + "\033[39m");
        this.colors.put("yellow",         "\033[33m" + character + "\033[39m");
        this.colors.put("blue",           "\033[34m" + character + "\033[39m");
        this.colors.put("magenta",        "\033[35m" + character + "\033[39m");
        this.colors.put("cyan",           "\033[36m" + character + "\033[39m");
        this.colors.put("white",          "\033[37m" + character + "\033[39m");

        this.colors.put("gray",           "\033[90m" + character + "\033[39m");
        this.colors.put("bright black",   "\033[90m" + character + "\033[39m");
        this.colors.put("grey",           "\033[90m" + character + "\033[39m");

        this.colors.put("bright red",     "\033[91m" + character + "\033[39m");
        this.colors.put("bright green",   "\033[92m" + character + "\033[39m");
        this.colors.put("bright yellow",  "\033[93m" + character + "\033[39m");
        this.colors.put("bright blue",    "\033[94m" + character + "\033[39m");
        this.colors.put("bright magenta", "\033[95m" + character + "\033[39m");
        this.colors.put("bright cyan",    "\033[96m" + character + "\033[39m");
        this.colors.put("bright white",   "\033[97m" + character + "\033[39m");

        this.setFullScreen(startColor);
    }

    public static void main(String[] args) {
        shittyTextRenderer shtr = new shittyTextRenderer("black", "█");
        int i;
        int j;
        int frames = 0;
        Object[] colors = shtr.colors.keySet().toArray();
        Random rand = new Random();
        double startTime = System.currentTimeMillis()/1000;
        double duration;

        while (true) {
            frames += 1;
            for (i=0; i<shtr.getRows(); i++){
                for (j=0; j<shtr.getCols(); j++){
                    //shtr.setColor(j, i, colors[rand.nextInt(colors.length)].toString());
                    shtr.setColor(j, i, colors[frames % colors.length].toString());
                }
            }
            //shtr.setFullScreen(colors[rand.nextInt(colors.length)].toString());
            shtr.display();
            duration = (System.currentTimeMillis()/1000) - startTime;
            System.out.print("fps: " + (frames/duration));
        }
    }
}

