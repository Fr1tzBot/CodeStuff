function beer = ferment(a, recipe, wort)
    %import constants
    constants

    %calculate maltose lbs (80% of grain by mass)
    maltose = 0.8 * recipe.grain;

    %notify user of inputs
    fprintf("Fermenting with %.2f gallons of wort, %.2f lbs yeast, and %.2f lbs maltose...\n", wort, recipe.yeast, maltose)

    %turn on ferment led
    a.writeDigitalPin(hwmap.leds.ferment, 1)

    %pause to simulate fermenting
    pause(1)

    simulateFerment(recipe, wort)

    %calculate sediment waste and beer output
    sediment = wort - recipe.gallons;
    beer = wort - sediment;

    %notify user of outputs
    fprintf("Produced %.2f gallons of sediment.\n", sediment)
    pause(1)
    fprintf("Produced %.2f gallons of beer\n\n", beer)
    pause(1)
end


function simulateFerment(recipe, wort)
    maltose = recipe.grain * 0.8;
    dt = 1;
    i = 1;
    time(1) = 0;
    sugar(1) = maltose / wort; %lbs/gal
    yeast(1) = recipe.yeast / wort; %lbs/gal
    abv(1) = 0;
    co2(1) = 0;

    consts.maxGrowth = 0.07; %/hr
    consts.yeastYield = 0.05; %yeast:sugar
    consts.yeastI = yeast(1);
    consts.sugarI = sugar(1);
    consts.saturationConc = 1.2; %lbs/gal
    consts.alchoholYield = -0.488;
    consts.co2Yield = -0.468;
    consts.sugarYield = -1/consts.yeastYield;

    while sugar(i) > (0.2 * sugar(1))
        yeastRate = getYeastRate(consts, yeast(i));
        sugarRate = yeastRate * consts.sugarYield;
        abvRate   = sugarRate * consts.alchoholYield;
        co2Rate   = sugarRate * consts.co2Yield;

        i = i + 1;

        yeast(i) = yeast(i - 1) + yeastRate * dt;
        sugar(i) = sugar(i - 1) + sugarRate * dt;
        abv(i) = abv(i - 1) + abvRate * dt;
        co2(i) = co2(i - 1) + co2Rate * dt;

        time(i) = time(i - 1) + dt;

        pause(0.1)
    end

    fprintf("Final ABV: %.2f percent\n", abv(end) / 6.534 * 100);
    pause(1)

    subplot(4, 1, 1)
    plot(time, sugar)
    title("Sugar Vs. Time")
    xlabel("Time (Hours)")
    ylabel("Sugar (lbs/gal)")

    subplot(4, 1, 2)
    plot(time, yeast)
    title("Yeast Vs. Time")
    xlabel("Time (Hours)")
    ylabel("Yeast (lbs/gal)")

    subplot(4, 1, 3)
    plot(time, abv)
    title("Alchohol vs Time")
    xlabel("Time (Hours)")
    ylabel("Alchohol (lbs/gal)")

    subplot(4, 1, 4)
    plot(time, co2)
    title("CO2 vs Time")
    xlabel("Time (Hours)")
    ylabel("CO2 (lbs/gal)")
end

