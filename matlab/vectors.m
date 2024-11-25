% Vector Math
% Name:  Fritz Geib
% Section: L13
% Team: 3

% Given:
x20 = [3, 9, 4, 7, 2];
b20 = [4, 2, 5, 6, 1];

% Create a new vector y20 that divides x20 by the scalar number 5
y20 = x20 / 5;
% Create a new vector c20 that divides each element of vector b20 by each corresponding element of vector x20
c20 = b20 ./ x20;
% Create a new vector z20 that raises the vector x20 to the power of 4
z20 = x20 .^ 4;
% Use pythagoreans theorm to calculate the distance between the two plotted points into the variable mydist
mydist = sqrt((x20(1) - b20(1))^2 + (x20(2) - b20(2))^2 + (x20(3) - b20(3))^2 + (x20(4) - b20(4))^2 + (x20(5) - b20(5))^2);
