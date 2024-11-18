% wind turbine code
% Author: Fritz Geib
% Date: 11/15/2024 2:17 AM
% Team: L13-3

%two formulas are used for this:
%P = v*a (watts = volts * amps)
%V = I*R (volts = amps * ohms)

a = arduino()
tic
t=0;

function current = solveForCurrent(voltage, resistance)
    current = voltage/resistance;
end

function power = solveForPower(voltage, current)
    power = voltage*current;
end

INTERNAL_RESISTANCE = 0.04*1000; %ohms (TODO find actual value)

time = [];
voltage = [];
power = [];

while t<10
    v = readVoltage(a, 'A0');
    % v = rand()*5;
    i = solveForCurrent(v, INTERNAL_RESISTANCE);
    p = solveForPower(v, i);

    t = toc;
    time(end+1) = t;
    voltage(end+1) = v;
    power(end+1) = p;
    pause(0.5)
end

%plot voltage vs time and power vs time in a subplot
figure
subplot(2,1,1)
plot(time, voltage, "r")
xlabel('Time (s)')
ylabel('Voltage (V)')
title('Voltage vs Time')
legend('Voltage')

subplot(2,1,2)
plot(time, power, "b")
xlabel('Time (s)')
ylabel('Power (W)')
title('Power vs Time')
legend('Power')

