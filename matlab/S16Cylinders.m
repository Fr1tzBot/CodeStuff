%You are in charge of pouring three cylindrical pillars for a building site. You need to know what total volume in ft^3 of concrete to order to get this job done.
%
%You are to create a script file that asks the user via finput statements the pertinent information (radius, height) needed to calculate the volume of three cylindrical pillars. Then you will create a separate function file with the volume equation that will be called into the script three times for the calculation of each pillar's volume. You will then program fprintf statements into the script that output to the user each pillar's volume, and how much total cement in ft^3 is needed to pour all three pillars.
%
%1) Create a script file that asks the user for radius and height in inches for each cylindrical column (r1, h1, r2, h2, r3, h3).
%
%2) Create a second function .m file that calculates the volume of a cylindrical pillar when given the inputs r and h. Make sure you pay attention to the proper syntax.
%
%3) After you have r and h from the user for three pillars, back in the script file, call in the function file three times to calculate the volumes of all three pillars. You will have different variable names for the two inputs, and the one output for each pillar.

clc

% Prompt user for radius and height of each cylinder
r1 = input('Enter the radius of the first cylinder in inches: ');
h1 = input('Enter the height of the first cylinder in inches: ');
r2 = input('Enter the radius of the second cylinder in inches: ');
h2 = input('Enter the height of the second cylinder in inches: ');
r3 = input('Enter the radius of the third cylinder in inches: ');
h3 = input('Enter the height of the third cylinder in inches: ');

% Call the function to calculate the volume of each cylinder
v1 = cylinderVolume(r1, h1);
v2 = cylinderVolume(r2, h2);
v3 = cylinderVolume(r3, h3);

% Calculate the total volume of concrete needed
totalVolume = v1 + v2 + v3;

% Display the volume of each cylinder and the total volume needed
fprintf('The volume of the first cylinder is %.2f ft^3.\n', v1);
fprintf('The volume of the second cylinder is %.2f ft^3.\n', v2);
fprintf('The volume of the third cylinder is %.2f ft^3.\n', v3);
fprintf('The total volume of concrete needed for all three cylinders is %.2f ft^3.\n', totalVolume);

