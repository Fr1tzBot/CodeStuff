clc
clear all

a = arduino();

pins.led.mill = 'D2';
pins.led.mash = 'D3';
pins.led.lauter = 'D4';
pins.led.boil = 'D5';
pins.led.gauge = 'D6';
pins.mc.dir = 'D7';
pins.mc.pwm = 'D8';

function setleds(status, leds, a)
    fields = fieldnames(leds);
    for i = 1:numel(fields)
        field = fields{i};
        value = leds.(field);
        a.writeDigitalPin(value, status{i})
    end
end

function runpump(speed, mc, a)
    if speed > 0
        a.writeDigitalPin(mc.dir, 1)
        a.writePWMDutyCycle(mc.pwm, 1)
    elseif speed < 0
        a.writeDigitalPin(mc.dir, 0)
        a.writePWMDutyCycle(mc.pwm, 1)
    else
        a.writePWMDutyCycle(mc.pwm, 0)
    end
end

setleds([0,0,0,0,0], pins.led, a)



