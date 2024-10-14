% incrediblyAdvancedCode.m: and incredibly advanced program wherein a digital
% input device is used to toggle two digital output pins, connected to
% light emitting diodes
% author: Fritz Geib
% date: 10/10/2024
% email: ftgeib@mtu.edu

clc
clear all

a = arduino()

a.configurePin("D10", "pullup")

toggle = 0;

while true
    if mod(toggle, 2) == 0
        a.writeDigitalPin("D2", 0);
        a.writeDigitalPin("D3", 1);
    else
        a.writeDigitalPin("D2", 1);
        a.writeDigitalPin("D3", 0);
    end

    if a.readDigitalPin("D10") == 0
        toggle = toggle + 1;
        while a.readDigitalPin("D10") == 0
            pause(0.01)
        end
    end
end
