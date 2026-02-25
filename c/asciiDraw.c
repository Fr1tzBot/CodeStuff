// Student stub code for ASCII Drawing assignment
//Name: Fritz Geib
//Description: Draws ascii art based on info in a file

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Initializes all the pixels of a image to black.
// You shouldn't need to modify this function!
void initImage(int width, int height, double image[width][height])
{
    //But what if I want to modify it?
    double* sp = &image[0][0];
    for (int i = 0; i < width * height; i++) {
        sp[i] = 0.0;
    }
}

//Prints The image from the provided image[][] array
void printImage(int width, int height, double image[width][height])
{
    //build header
    char header[width+1];
    header[width] = '\0';
    for (int i = 0; i < width; i++) { header[i] = '-'; }
    printf("+%s+\n", header);

    const char chars[] = " .:-=+*#%@";
    char to_print[width+1];
    to_print[width] = '\0';

    //Change left and right boundaries to pipes
    for (int i = 0; i < width * height; i++) {
        int j = i % width;

        //Convert val to an int index in our char list
        int val = (int) (image[j][i/width] * 10);

        //Ensure values > 9 get mapped back down to 9
        val = val > 9 ? 9 : val;
        to_print[j] = chars[val];

        //Once we've finished filling the array we print the line
        //Note that we didn't touch the last char (the null term)
        if (j == width - 1) {
            printf("|%s|\n", to_print);
        }
    }

    printf("+%s+\n", header);
}

//Sets a single point in the image[][] array to the specified color
void drawPoint(int width, int height, double image[width][height],
               int x, int y, double color)
{
    if (x >= width || y >= height || y < 0 || x < 0) {return;}
    image[x][y] = color;
}

//Draw a Rectangle with the specified width and height at the given x and y
void drawRectangle(int width, int height, double image[width][height],
                   int x, int y, int rectWidth, int rectHeight, double color)
{
    //Handle too small inputs
    if (rectWidth <= 0 || rectHeight <= 0) { return; }

    //Handle too big inputs
    if (x >= width || y >= height) { return; }

    //A cursed nested loop....
    //Wrote it with pointers and stuff first, but
    //still needed a nested while to populate each row
    for (int xi = x; xi < x+rectWidth; xi++) {
        for (int yi = y; yi < y+rectHeight; yi++) {
            drawPoint(width, height, image, xi, yi, color);
        }
    }
}

//Sets whole image to 0 or 1 based on the given threshold
void convertToBlackAndWhite(int width, int height, double image[width][height],
                            double threshold)
{
    double* sp = &image[0][0];
    for (int i = 0; i < width * height; i++) {
        sp[i] = sp[i] < threshold ? 0.0 : 1.0;
    }
}

//Draw an approximation of a line from the start point to the end point
void drawLine(int width, int height, double image[width][height],
              int x1, int y1, int x2, int y2, double color)
{
    int dx = x2 - x1;
    int dy = y2 - y1;

    int steps = abs(dx) > abs(dy) ? abs(dx) : abs(dy);

    double Xinc = dx / (double) steps;
    double Yinc = dy / (double) steps;

    double x = x1;
    double y = y1;

    for (int i = 0; i <= steps; i++) {
        drawPoint(width, height, image, round(x), round(y), color);
        x += Xinc;
        y += Yinc;
    }
}

//Calculate the min, max, mean, and stdev for the image
void printStats(int width, int height, double image[width][height])
{
    double* sp = &image[0][0];
    double min = sp[0];
    double max = sp[0];
    double sum = sp[0];
    double sumSq = sum * sum;
    int n = width * height;

    //We start loop at 1 because we already processed sp[0]
    for (int i = 1; i < n; i++) {
        double val = sp[i];
        if (val < min) { min = val; }
        if (val > max) { max = val; }
        sum += val;
        sumSq += val * val;
    }

    double mean = sum / n;
    double sd = sqrt((sumSq/n)-(mean*mean));

    printf("Color range [%.2lf, %.2lf], mean %.4lf, sd %.4lf\n",
           min, max, mean, sd);
}

//Paint bucket a region with the given color
void floodFill(int width, int height, double image[width][height],
               int x, int y, double color)
{
    if (x >= width || y >= height || x < 0 || y < 0 || image[x][y] >= color) {return;}
    drawPoint(width, height, image, x, y, color);
    floodFill(width, height, image, x+1, y, color);
    floodFill(width, height, image, x, y+1, color);
    floodFill(width, height, image, x-1, y, color);
    floodFill(width, height, image, x, y-1, color);
}

// Print the resulting grayscale image as ASCII art.
// Dont change other things in the main function.
int main(int argc, char** argv)
{
    FILE* fp;
    if (argc > 2)
    {
        printf("Usage: Draw <filename>\n");
        return 0;
    } else if (argc == 1) {
        fp = stdin;
    } else {
        fp = fopen(argv[1], "r");
    }
    if (fp == NULL)
    {
        printf("ERROR: failed to open input file '%s'!\n", argv[1]);
        return 0;
    }

    // Read in the size of the drawing canvas
    int width = 0;
    int height = 0;

    // The fscanf function returns a integer with the number of read in variables.
    // The main program uses this result to check for badly formatted input.
    // The fscanf function can read in multiple variables in one call  (see the lecture slides).
    int result = fscanf(fp, "%d %d", &width, &height);

    // Program only supports images that are 1x1 or bigger
    if ((width <= 0) || (height <= 0) || (result != 2))
    {
        printf("ERROR: failed to read width and height!\n");

        fclose(fp);

        return 0;
    }

    // Create an 2D array and initialize all the greyscale values to 0.0.
    // The first dimension is the x-coordinate.
    // The second dimension is the y-coordinate
    double image[width][height];
    initImage(width, height, image);

    char command = '\0';
    double color = 0.0;

    // Keep reading in drawing comands until we reach the end of the input
    while (fscanf(fp, " %c", &command) == 1)
    {
        switch (command)
        {
            case 'p':
            {
                // Draw a point, read in: x, y, color
                int x = 0;
                int y = 0;

                result = fscanf(fp, "%d %d %lf", &x, &y, &color);
                if (result != 3)
                {
                    printf("ERROR: invalid point command!\n");
                    return 0;
                }
                drawPoint(width, height, image, x, y, color);
                break;
            }
            case 'r':
            {
                // Draw a rectangle, read in: x, y, w, h, color
                int left = 0;
                int top = 0;
                int rectangleWidth = 0;
                int rectangleHeight = 0;

                result = fscanf(fp, "%d %d %d %d %lf",
                                &left, &top,
                                &rectangleWidth,
                                &rectangleHeight,
                                &color);
                if (result != 5)
                {
                    printf("ERROR: invalid rectangle command!\n");
                    return 0;
                }
                drawRectangle(width, height, image, left, top, rectangleWidth, rectangleHeight, color);
                break;
            }
            case 'b':
            {
                // Convert to black and white
                double threshold = 0.0;

                result = fscanf(fp, "%lf", &threshold);
                if (result != 1)
                {
                    printf("ERROR: invalid black and white command!\n");
                    return 0;
                }
                convertToBlackAndWhite(width, height, image, threshold);
                break;
            }

            case 'l':
            {
                // Draw a line, read in x1, y1, x2, y2, color
                int x1 = 0;
                int y1 = 0;
                int x2 = 0;
                int y2 = 0;

                result = fscanf(fp, "%d %d %d %d %lf", &x1, &y1, &x2, &y2,
                                &color);
                if (result != 5)
                {
                    printf("ERROR: invalid line command!\n");
                    return 0;
                }
                drawLine(width, height, image, x1, y1, x2, y2, color);
                break;
            }
            case 'f':
            {
                // Flood fill a color in, read in: x, y, color
                int x = 0;
                int y = 0;

                result = fscanf(fp, "%d %d %lf", &x, &y, &color);                if (result != 3)
                {
                    printf("ERROR: invalid flood fill command!\n");
                    return 0;
                }
                floodFill(width, height, image, x, y, color);
                break;

            }
            default:
            {
                printf("ERROR: unknown command!\n");
                return 0;
            }
        }
    }

    fclose(fp);

    // Print the final image
    printImage(width, height, image);

    // Finally display some statistics about the image
    printStats(width, height, image);

    return 0;
}

