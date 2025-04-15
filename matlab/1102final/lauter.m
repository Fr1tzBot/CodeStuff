function wort = lauter(a, crushedGrain, wort)
    %import constants
    constants

    %set sparge water equal to 50% of the grain
    spargeWater = 0.5 * crushedGrain;

    %notify user of inputs
    fprintf("Lautering %.2f gallons of wort with %.2f gallons of sparge water\n", wort, spargeWater)

    %turn on lauter led
    a.writeDigitalPin(hwmap.leds.lauter, 1)

    %pause to simulated lautering
    pause(1)

    %notify user of outputs
    fprintf("Spent %.2f lbs of grain.\n", crushedGrain)
    pause(1)

    %calculate waste water in grain
    grainWater = 0.1 * crushedGrain;
    fprintf("Removed %.2f gallons of water with grain.\n", grainWater)
    pause(1)

    %calculate output wort
    wort = wort + spargeWater - grainWater;
    fprintf("Produced %.2f Gallons of wort.\n\n", wort)
    pause(1)
end

