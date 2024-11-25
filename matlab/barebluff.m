% barebluff.m: do some stuff that may or may not involve a bluff or a bear
% Name: Fritz Geib
% Date: 11/10/2024 5:00 AM
% Section: L13-3

% Import data
[time, lat, long, alt, spd] = readvars("Bare_Bluff_Position.xlsx");

% Create map
figure
plot(long, lat)
title('Map of Bare Bluff Trail')
xlabel('Longitude')
ylabel('Latitude')

% Create plots
figure
subplot(2,1,1)
plot(time, alt)
title('Altitude as a Function of Time')
xlabel('Time')
ylabel('Altitude')
subplot(2,1,2)
plot(time, spd)
title('Speed as a Function of Time')
xlabel('Time')
ylabel('Speed')



