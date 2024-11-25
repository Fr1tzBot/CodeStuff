% Wind Turbine.m
% Author: Fritz Geib
% Section L13-3
clc
clear

bladeLength = 3.25; % meters
airDensity = 1.225; % kg/m^3
sweptArea = pi * bladeLength^2; % m^2
[windSpeed, realPower] = readvars("Wind_Data.xlsx");

theoreticalPower = zeros(1, length(windSpeed));

% generate theoretical power data
for i = 1:length(windSpeed)
    theoreticalPower(i) = 0.5 * airDensity * sweptArea * windSpeed(i)^3;
end

% plot the data
hold on
plot(windSpeed, realPower, 'r', windSpeed, theoreticalPower, 'b')
grid on
xlabel('Wind Speed (m/s)')
ylabel('Power (W)')
title('Wind Turbine Power vs Wind Speed')
legend('Real Power', 'Theoretical Power')
hold off

