% a script that steps through a vector of altitudes (0 to 48000 meters in steps of 1000 meters) and outputs the temperature for that altitude in a plot.
% Use a for loop and if statements to choose the correct equations to use. You should calculate the temperature as a vector element (HINT: remember how we build vectors in for loops).
% Troposphere: A < 11,000 m
% T  = 15.04 - 0.00649 * A
% Stratosphere: 11,000 m <= A < 25,000 m
% T = -56.46
% Upper Stratosphere: 25,000 m <= A < 50,000 m
% T = -131.21 + 0.00299 * A
% Create a plot with the temperature on the x axis and altitude on the y-axis.
% Troposphere - plot as blue asterisk
% Lower Stratosphere - plot as black asterisk
%Upper Stratosphere - plot as magenta asterisk
% NOTE: altitude should be on the y-axis.
% Create 3 separate fprintf statements that report to the user how many temperature measurements are in the troposphere, lower stratosphere, and upper stratosphere

clc
clear

% Define the vector of altitudes
A = 0:1000:48000;

% Initialize the temperature vector
T = zeros(size(A));

a = arduino();

% Loop through the altitudes
for i = 1:length(A)
    % Check the altitude range
    if A(i) < 11000
        % Troposphere
        T(i) = 15.04 - 0.00649 * A(i);
    elseif A(i) < 25000
        % Stratosphere
        T(i) = -56.46;
    else
        % Upper Stratosphere
        T(i) = -131.21 + 0.00299 * A(i);
    end

    a.writeDigitalPin('D13', mod(i, 2))
    pause(0.1)
end

% Plot the temperature vs. altitude
figure;
hold on;
plot(T(A < 11000), A(A < 11000), 'b*');
plot(T(A >= 11000 & A < 25000), A(A >= 11000 & A < 25000), 'k*');
plot(T(A >= 25000), A(A >= 25000), 'm*');
xlabel('Temperature (°C)');
ylabel('Altitude (m)');
title('Temperature vs. Altitude');
legend('Troposphere', 'Lower Stratosphere', 'Upper Stratosphere');
hold off;

% Count the number of measurements in each region
num_troposphere = sum(A < 11000);
num_lower_stratosphere = sum(A >= 11000 & A < 25000);
num_upper_stratosphere = sum(A >= 25000);

a.writeDigitalPin('D13', 0)