clc
clear

% Load the data
data = readmatrix('~/Downloads/solar_panel_data.xlsx');

% Extract the data
day = data(:,1);
irradiance = data(:,2);
energy = data(:,3);

%remove energy values < 0
day = day(energy >= 0);
irradiance = irradiance(energy >= 0);
energy = energy(energy >= 0);

% find mean energy on days with irradiance > 400
mean_energy = mean(energy(irradiance > 400));

% find the mean energy on days with irradiance < 400
mean_energy_low_irradiance = mean(energy(irradiance < 400));

%plot the data with a line at 400 W/m^2
figure
scatter(irradiance, energy, 'filled')
hold on
plot([400 400], [0 max(energy)], 'r--')
xlabel('Irradiance (W/m^2)')
ylabel('Energy (kWh)')
title('Energy vs Irradiance')
legend('Data', 'Irradiance = 400 W/m^2')

