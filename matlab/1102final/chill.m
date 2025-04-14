function wort = chill(a, wort)
    %import constants
    constants

    %notify user of input
    fprintf("Chilling %.2f gallons of wort.\n", wort)

    %turn on chill led
    a.writeDigitalPin(hwmap.leds.chill, 1)

    %pause to simulate chilling
    pause(1)

    %notify user of chilled output
    fprintf("Produced %.2f gallons of wort.\n\n", wort)
end

