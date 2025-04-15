function wort = mash(a, crushedGrain)
    constants
    water = 0.25 * crushedGrain;
    fprintf("Mashing %.2f lbs of grain with %.2f gallons of water...\n", crushedGrain, water)
    a.writeDigitalPin(hwmap.leds.mash, 1)
    wort = water;
    pause(1)
    fprintf("Created wort with %.2f gallons of liquid.\n\n", water)
    pause(1)
end

