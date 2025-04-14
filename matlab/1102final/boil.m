function wort = boil(a, wort)
    %import constants
    constants

    %TODO: make algorithms to avoid hard coding these two
    topUpWater = 2;
    evapWater = 3;

    %give input notifications
    fprintf("Boiling %.2f gallons of wort...\n", wort)
    fprintf("Added %.2f gallons of top up water.\n", topUpWater)

    %turn on boil led
    a.writeDigitalPin(hwmap.leds.boil, 1)

    %pause for a simulated amount of time
    pause(1)

    %calculate output wort
    wort = wort + topUpWater - evapWater;

    %notify user of boiled wort
    fprintf("%.2f gallons of water evaporated while boiling.\n", evapWater)
    fprintf("Produced %.2f gallons of wort.\n\n", wort)
end

