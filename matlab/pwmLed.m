clc
clear all

a = arduino()

RED = 'D2';
GREEN = 'D4';
BLUE = 'D3';
SERVO = servo(a, 'D5')

a.configurePin(RED, 'DigitalOutput')
a.configurePin(GREEN, 'DigitalOutput')
a.configurePin(BLUE, 'DigitalOutput')
for i = 1:10
    % a.writeDigitalPin(RED, 1)
    % a.writeDigitalPin(RED, 0)
    % a.writeDigitalPin(GREEN, 1)
    % a.writeDigitalPin(GREEN, 0)
    writePosition(SERVO, 1)
    pause(1)
    writePosition(SERVO, 0)
    pause(1)
end
exit
