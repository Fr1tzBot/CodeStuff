% Use a button and joystick to send values to MATLAB and accomplish a task
% 1. Button - Use a while loop that runs until the button is pushed
% 2. Joystick - Read and display the X and Y coordinates of the joystick.

clc
clear

a = arduino();

button = 'D5';
joystickX = 'A1';
joystickY = 'A0';

configurePin(a, button, 'Pullup');
configurePin(a, joystickX, 'AnalogInput');
configurePin(a, joystickY, 'AnalogInput');

%fprintf("%d", readDigitalPin(a, button))

while readDigitalPin(a, button)==1
    x = readVoltage(a, joystickX);
    y = readVoltage(a, joystickY);
    fprintf('X: %f, Y: %f\n', (x-2.5)/2.5, (y-2.5)/2.5);
    pause(0.1);
end
