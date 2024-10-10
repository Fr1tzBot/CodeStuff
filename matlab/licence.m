% author: Fritz Geib
% date: 10/10/24
% email: ftgeib@mtu.edu

clc

age = input("Enter your age in years: ");

if age < 14.75
    licenseLevel = 0;
elseif age < 16
    licenseLevel = 1;
elseif age < 17
    licenseLevel = 2;
else
    licenseLevel = 3;
end

if licenseLevel > 0
    fprintf("License Level %d.\n", licenseLevel);
else
    fprintf("You are too young to drive.\n");
end
