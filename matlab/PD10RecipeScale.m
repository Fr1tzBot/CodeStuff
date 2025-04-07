clc
clear all

function scaledRecipe = scaleRecipe(baseRecipe, scaledRecipe)
    fields = fieldnames(baseRecipe);
    for i = 1:numel(fields)
        field = fields{i};
        value = baseRecipe.(field);
        if ismember(field, ["gallons", "hopcount", "hopoz", "hopaa", "hopbt"])
            continue
        else
            scaledRecipe.(field) = value * scaledRecipe.scaleFactor;
        end
    end
end

baseRecipe.gallons = input("How Many Gallons in your homebrew batch (5)? ");
scaled.barrels = input("How many barrels in your full size batch (10)? ");
baseRecipe.grain = input("How many pounds of grain in your homebrew batch (12)? ");
baseRecipe.hopcount = input("How many hops are you using (3)?");
baseRecipe.hopoz = zeros(1, baseRecipe.hopcount);
baseRecipe.hopaa = zeros(1, baseRecipe.hopcount);
baseRecipe.hopbt = zeros(1, baseRecipe.hopcount);

for i = 1:baseRecipe.hopcount
    baseRecipe.hopoz(i) = input("How many oz of hop " + i + "? ");
    baseRecipe.hopaa(i) = input("What is the Alpha Acid of hop " + i + "? ");
    baseRecipe.hopbt(i) = input("What is the Boil Time of hop " + i + " (minutes)? ");
end

baseRecipe.boiladd = input("how many gallons of water added to boil in homebrew batch? ");
baseRecipe.evap = input("how many gallons of water evaporated in the homebrew boil? ");
debug()

baseRecipe.barrels = baseRecipe.gallons / 31.0;
% fprintf("Barrels: %0.2f\n", baseRecipe.barrels)
baseRecipe.mashWater = 0.25 * baseRecipe.grain;
% fprintf("Mash Water (gallons): %0.2f\n", baseRecipe.mashWater)
baseRecipe.lauterWaterAdd = 0.5 * baseRecipe.grain;
% fprintf("lauter Water added (gallons): %0.2f\n", baseRecipe.lauterWaterAdd)
baseRecipe.lauterWaterRem = 0.1 * baseRecipe.grain;
baseRecipe.wortToBoil = baseRecipe.mashWater + baseRecipe.lauterWaterAdd - baseRecipe.lauterWaterRem;
baseRecipe.boiledWort = baseRecipe.wortToBoil + 0 - baseRecipe.evap;
baseRecipe.trub = 0.1 * baseRecipe.boiledWort;
baseRecipe.wortToChill = baseRecipe.boiledWort - baseRecipe.trub;
baseRecipe.wortToFerment = baseRecipe.wortToChill;
baseRecipe.maltose = 0.8 * baseRecipe.grain;
baseRecipe.sediment = baseRecipe.wortToFerment - baseRecipe.gallons;
baseRecipe.beer = baseRecipe.wortToFerment - baseRecipe.sediment;
fprintf("Homebrew recipe calculated values:\n")
disp(baseRecipe)
scaled.gallons = scaled.barrels * 31;
scaled.scaleFactor = scaled.gallons / baseRecipe.gallons;

scaled = scaleRecipe(baseRecipe, scaled);
fprintf("Scaled Up Recipe Calculated values:\n")
disp(scaled)

