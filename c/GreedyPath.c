//Author: Fritz Geib
//Email: ftgeib@mtu,edu
//Description: A program which recieves a list of points, prints their bounding box,
//             and a path between them, and the distance travelled on that path.

#include <stdlib.h>
#include <math.h>
#include <limits.h>
#include <stdio.h>
#include <time.h>
#include <stdbool.h>

//Returns the max double in an array
double max(double a[], int len) {
    double max = INT_MIN;
    for (int i = 0; i < len; i++) {
        if (a[i] > max) {
            max = a[i];
        }
    }
    return max;
}

//Returns the index of the min double in an array
int minI(double a[], int len) {
    double min = INT_MAX;
    int index = -1;
    for (int i = 0; i < len; i++) {
        if (a[i] < min) {
            min = a[i];
            index = i;
        }
    }
    return index;
}

//Returns the min double in an array
double min(double a[], int len) {
    //Repeating yourself is redundant
    return a[minI(a, len)];
}

//Calculates the distance from point (X, Y)
//To each point in X[] and Y[]
//Skips points that are marked in visited[]
//Modifies out[] in place
void dist(double X, double Y, double x[], double y[], bool visited[], double out[], int len) {
    for (int i = 0; i < len; i++) {
        //If we have already visited this point,
        //Set distance to a really high number so it doesn't get picked
        if ( visited[i]) { out[i] = INT_MAX; }
        else {
            //Otherwise pythagorean theorum our way to victory
            double xDist = X - x[i];
            double yDist = Y - y[i];
            xDist *= xDist;
            yDist *= yDist;
            out[i] = sqrt(xDist+yDist);
        }
    }
}

int main(void)
{
    //Take input
    int numPoints;
    scanf("%d", &numPoints);
    double x[numPoints];
    double y[numPoints];
    double X;
    double Y;

    //Read each line of input
    for (int i = 0; i < numPoints; i++) {
        scanf("%lf %lf", &X, &Y);
        x[i] = X;
        y[i] = Y;
    }

    //One time use variables for readability
    double minx = min(x, numPoints);
    double maxx = max(x, numPoints);

    double miny = min(y, numPoints);
    double maxy = max(y, numPoints);

    //Print out bounding box, followed by number of points read
    printf("%lf %lf\n%lf %lf\n\n%d\n", minx, miny, maxx, maxy, numPoints);

    //Create and initialize our array for tracking whether each point is visited
    bool visited[numPoints];
    for (int i = 0; i < numPoints; i++) { visited[i] = false; }

    //Create vars for tracking distance
    double distances[numPoints];
    double distance = 0;

    //X and y get initialized to the first point read
    X = x[0];
    Y = y[0];

    int minIndex;

    for (int i = 0; i < numPoints; i++) {
        //Solve distance to each point and find the lowest one
        dist(X, Y, x, y, visited, distances, numPoints);
        minIndex = minI(distances, numPoints);

        //Update vars for next iteration and print visited point
        visited[minIndex] = true;
        distance += distances[minIndex];
        X = x[minIndex];
        Y = y[minIndex];
        printf("%lf %lf\n", X, Y);
    }

    //Finally print total distance travelled
    printf("\n%lf\n", distance);

    return 0;
}
