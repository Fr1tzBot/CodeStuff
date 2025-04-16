clc
clear all

a = arduino();


a.writeDigitalPin('D11', 1) %motor pwr
a.writeDigitalPin('D12', 0) %motor dir
pause(1)
a.writeDigitalPin('D2', 1)
a.writeDigitalPin('D3', 1)
a.writeDigitalPin('D4', 1)
a.writeDigitalPin('D5', 1)
a.writeDigitalPin('D6', 1)
a.writeDigitalPin('D7', 1)
s = servo(a, 'D9');
fprintf("%f\n", a.readVoltage('A0'))
writePosition(s, 1)
pause(30)
a.writeDigitalPin('D2', 0)
a.writeDigitalPin('D3', 0)
a.writeDigitalPin('D4', 0)
a.writeDigitalPin('D5', 0)
a.writeDigitalPin('D6', 0)
a.writeDigitalPin('D7', 0)
a.writeDigitalPin('D11',0) %motor pwr
a.writeDigitalPin('D12', 0) %motor dir
writePosition(s,0)
fprintf("%f\n", a.readVoltage('A0'))
exit

