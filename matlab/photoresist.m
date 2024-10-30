% Connect
clear
a = arduino(); % Connect to the first Arduino Seen

% Set pin D9 for yellow LED
yellowLEDPin = 'D9';
configurePin(a, yellowLEDPin, 'DigitalOutput'); % Configure pin for yellow LED

% Measure
Time = []; tic(); % Start a timer for measuring
LightMeasurement = []; % Start a vector for data
disp("Start") % Notify user of Start
threshold = 1.75; % Define the level to use as a threshold
for i = 1:100 % Loop to collect measurements
disp(i); % Identify which measurement we are collecting
Time(i) = toc(); % Save the time elapsed in seconds of the measurement
LightMeasurement(i) = a.readVoltage("A0"); % Save/Collect the Data
% Check if the light value is below the threshold, turn on yellow LED
if LightMeasurement(i) < threshold
writeDigitalPin(a, yellowLEDPin, 1); % Turn on the yellow LED
else
writeDigitalPin(a, yellowLEDPin, 0); % Turn off the yellow LED
end
end
disp("end") % Notify user of end

% Plot
figure; % Create a new figure window
plot(Time, LightMeasurement, 'b*') % Place the data in the figure

% Analysis
% Count the number of times the light drops past the threshold
count = 0; % Create a variable to count
for i = 2:length(LightMeasurement) % Starting at the second measurement
if LightMeasurement(i)<threshold && LightMeasurement(i-1)>threshold %% If this measurement crosses the threshold line
count = count + 1; % If true, crossing, then increase the count by 1
end
end % Loop to the next measurement value

% Plot a Threshold line
hold on; % Hold on to previous plots to stack the plots together
plot([min(Time), max(Time)], [threshold, threshold],'r--'); % Plot a line for the threshold

% Output a user-readable result
UserStatus = sprintf("The light threshold was crossed %.f times", count); % Create a string to display the result
disp(UserStatus); % Print the string to the display
