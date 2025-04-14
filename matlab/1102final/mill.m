function chrushedGrain = mill(rawGrain)
    %notify user of input
    fprintf("Milling %.2f lbs of Grain...\n", rawGrain)

    %pause to simulate milling
    pause(1)

    %notify user of outputs
    chrushedGrain = rawGrain;
    fprintf("Crushed %d lbs of grain\n\n", chrushedGrain)
end

