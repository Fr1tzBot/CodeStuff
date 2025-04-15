function pump(a, on)
    %import constants
    constants

    if on
        %turn one of the motor pins on, based on the set motor invert
        if motorInvert
            p = hwmap.pump.pin1;
        else
            p = hwmap.pump.pin2;
        end
        a.writeDigitalPin(p, 1);
    else
        a.writeDigitalPin(hwmap.pump.pin1, 0)
        a.writeDigitalPin(hwmap.pump.pin2, 0)
    end
end

