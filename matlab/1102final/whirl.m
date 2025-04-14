function wort = whirl(a, wort)
    %import constants
    constants

    %notify user of inputs
    fprintf("Whirlpooling %.2f Gallons of wort...\n", wort)

    %turn on whirl led
    a.writeDigitalPin(hwmap.leds.whirl, 1)

    %pause to simulate whirlpooling
    pause(1)

    %calculate outputs
    trub = 0.1 * wort;
    wort = wort-trub;

    %notify user of outputs
    fprintf("Produced %.2f gallons of trub.\n", trub)
    fprintf("Produced %.2f gallons of wort.\n\n", wort)
end

