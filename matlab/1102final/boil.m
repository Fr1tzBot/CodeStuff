function wort = boil(a, recipe, wort)
    %import constants
    constants

    %TODO: make algorithms to avoid hard coding these two
    topUpWater = 2;
    evapWater = 3;

    %give input notifications
    fprintf("Boiling %.2f gallons of wort...\n", wort)
    pause(1)
    fprintf("Added %.2f gallons of top up water.\n", topUpWater)
    pause(1)

    totalIbu = 0;
    for i= 1:numel(recipe.hops.names)
        fprintf("Added %.2f lbs of hop %s after %d minutes of boil time.\n", recipe.hops.oz(i)/16, recipe.hops.names(i), recipe.hops.bt(i))
        util = 0.17691 + (0.94415 * recipe.hops.bt(i)) - (0.015027 * recipe.hops.bt(i)^2) + (0.00011369 * recipe.hops.bt(i)^3) - (0.00000033005 * recipe.hops.bt(i)^4);
        totalIbu = totalIbu + (util * recipe.hops.aa(i) * recipe.hops.oz(i) / recipe.gallons);
        pause(1)
    end

    %turn on boil led
    a.writeDigitalPin(hwmap.leds.boil, 1)

    %pause for a simulated amount of time
    pause(1)

    %calculate output wort
    wort = wort + topUpWater - evapWater;

    %notify user of boiled wort
    fprintf("Boiled for %d minutes\n", max(recipe.hops.bt))
    pause(1)
    fprintf("%.2f gallons of water evaporated while boiling.\n", evapWater)
    pause(1)
    fprintf("Total IBU: %.2f\n", totalIbu)
    pause(1)
    fprintf("Produced %.2f gallons of wort.\n\n", wort)
    pause(1)
end

