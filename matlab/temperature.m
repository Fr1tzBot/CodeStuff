% temperature.m: a for loop to determine the expected temperature change of a 100 g object made of silver when various amounts of heat are applied to the object, saving the result in the vector dT.
% Using the equation dT=Q/(m*c), where Q is [13, 19, 28, 44, 52, 60] m = 100 and c = 0.24.
% author: Fritz Geib
% date: 10/15/2024
% email: ftgeib@mtu.edu

% Initialize variables
Q = [13, 19, 28, 44, 52, 60]; % matrix of 6 Joules
m = 100; % 100 grams
c = 0.24; % 0.24 J/gC
dT = zeros(1,6); % a blank vector to store the results

% loop through each value in Q and calculate dT
for i = 1:length(Q)
    dT(i) = Q(i)/(m*c);
end

% Display the results
disp(dT)
