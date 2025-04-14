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

