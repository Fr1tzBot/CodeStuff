function [a, s] = initarduino
    %import constants
    constants

    %initialize arduino object
    a = arduino()

    %initialize led and pump output pins
    initpins(a, hwmap.leds)
    initpins(a, hwmap.pump)

    %set thermistor pin up as analog input
    a.configurePin(hwmap.thermistor, "AnalogInput")

    %create servo object to be returned
    s = servo(a, hwmap.gaugeServo);
    clc
end

function initpins(a, pins)
    %pull pin names into an array
    fields = fieldnames(pins);

    %iterate through the created array
    for i = 1:numel(fields)
        %set name to the selected item
        name = fields{1};

        %set pin to the pin corresponding to the selected name
        pin = pins.(name);

        %configure pin as digital output, and ensure it is low
        a.configurePin(pin, "DigitalOutput")
        a.writeDigitalPin(pin, 0)

        %debug message (in green)
        fprintf("\033[32mInitialized pin %s (%s).\033[0m\n", name, pin)
    end
end
