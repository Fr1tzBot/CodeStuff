function store(beer)
    %convert gallons to barrels
    barrels = beer / 31.0;

    %notify user how much beer is being stored
    fprintf("Storing %.2f Gallons of beer (%.2f barrels)\n", beer, barrels)
end
