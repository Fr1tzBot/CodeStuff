function beer = ferment(a, crushedGrain, yeast, wort, batch)
    %import constants
    constants

    %calculate maltose lbs (80% of grain by mass)
    maltose = 0.8 * crushedGrain;

    %notify user of inputs
    fprintf("Fermenting with %.2f gallons of wort, %.2f lbs yeast, and %.2f lbs maltose...\n", wort, yeast, maltose)

    %turn on ferment led
    a.writeDigitalPin(hwmap.leds.ferment, 1)

    %pause to simulate fermenting
    pause(1)

    %calculate sediment waste and beer output
    sediment = wort - batch;
    beer = wort - sediment;

    %notify user of outputs
    fprintf("Produced %.2f gallons of sediment.\n", sediment)
    fprintf("Produced %.2f gallons of beer\n\n", beer)
end


function getYeastRate(yeastGrams, wort, grain)
    maltose = grain * 0.8;
    dt = 1;
    i = 1;
    hour(1) = 0;
    sugar(1) = maltose / wort;
    yeast(1) = yeastGrams / wort;
    abv(1) = 0;
    co2(1) = 0;

    while sugar(i) > (0.2 * sugar(1))
        yeast_rate=((.07*((.05)*(sugar(1))+(yeast(1))-yeast(i)))/(1.2*.05+.05*(sugar(1))+yeast(1)-yeast(i)))*yeast(i);
        sugarRate=-yeast_rate/.05;
        abvRate=-yeast_rate*.488;
        co2Rate=-yeast_rate*.468;

        i = i + 1;

        yeast(i)=yeast(i-1)+yeastRate*dt;
        sugar(i)=sugar(i-1)+sugarRate*dt;
        abv(i)=abv(i-1)+abvRate*dt;
        co2(i)=co2(i-1)+co2Rate*dt;

        hour(i) = hour(i-1)*dt;
    end

    hold on
    plot(hour, sugar)
    plot(hour, yeast)
    plot(hour, abv)
    plot(hour, co2)
    hold off
end

