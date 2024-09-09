% Debug Assignment

% program you get to debug!!!
% Fritz Geib
% Section L13_3
% LEAP Week 3
% ENG1101 Fall 2024, 09/09/2024

% default shape dimensions
X = 2 %width
Y = 3 %depth
Z = 9 %height
r = 4.5 %radius
a = 1/4 %edge length

% volume of a cone
V_c = pi * (r^2) * (Z/3)

% area of a square
A_s = X * Y

% volume of a cube
V_c = Z * X * Y

% summed volume of a dodecahedron and spere
V_d = ((15 + 7*sqrt(5))/4)*(a^3)
V_s = (4/3)*pi*(r^3)
V_sum = V_s + V_d

%display sum of dodecahedron and sphere to user
disp(V_sum)

%display colume of cone
disp(V_c)


