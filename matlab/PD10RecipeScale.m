clc
clear all

% scaleRecipe: return a scaled up version of a given recipe
function scaledRecipe = scaleRecipe(baseRecipe, scaledRecipe)
    fields = fieldnames(baseRecipe); % pull struct fields from baseRecipe struct
    for i = 1:numel(fields)
        field = fields{i}; %assign "field" to the selected field
        value = baseRecipe.(field); %assign "value" to the corresponding value
        if ~ ismember(field, ["gallons", "hopcount", "hopoz", "hopaa", "hopbt"]) %skip values that don't need to be scaled
            scaledRecipe.(field) = value * scaledRecipe.scaleFactor; %assign scaled values to scaledRecipe
        end
    end
end

%prompt user to fill in basic inputs
baseRecipe.gallons = input("How Many Gallons in your homebrew batch (5)? ");
scaled.barrels = input("How many barrels in your full size batch (10)? ");
baseRecipe.grain = input("How many pounds of grain in your homebrew batch (12)? ");
baseRecipe.hopcount = input("How many hops are you using (3)?");

%initialize hop arrays
baseRecipe.hopoz = zeros(1, baseRecipe.hopcount);
baseRecipe.hopaa = zeros(1, baseRecipe.hopcount);
baseRecipe.hopbt = zeros(1, baseRecipe.hopcount);

%populate hop arrays with user input
for i = 1:baseRecipe.hopcount
    baseRecipe.hopoz(i) = input("How many oz of hop " + i + "? ");
    baseRecipe.hopaa(i) = input("What is the Alpha Acid of hop " + i + "? ");
    baseRecipe.hopbt(i) = input("What is the Boil Time of hop " + i + " (minutes)? ");
end

%last two user inputs
baseRecipe.boiladd = input("how many gallons of water added to boil in homebrew batch? ");
baseRecipe.evap = input("how many gallons of water evaporated in the homebrew boil? ");

%perform recipe calculations
baseRecipe.barrels = baseRecipe.gallons / 31.0;
baseRecipe.mashWater = 0.25 * baseRecipe.grain;
baseRecipe.lauterWaterAdd = 0.5 * baseRecipe.grain;
baseRecipe.lauterWaterRem = 0.1 * baseRecipe.grain;
baseRecipe.wortToBoil = baseRecipe.mashWater + baseRecipe.lauterWaterAdd - baseRecipe.lauterWaterRem;
baseRecipe.boiledWort = baseRecipe.wortToBoil + 0 - baseRecipe.evap;
baseRecipe.trub = 0.1 * baseRecipe.boiledWort;
baseRecipe.wortToChill = baseRecipe.boiledWort - baseRecipe.trub;
baseRecipe.wortToFerment = baseRecipe.wortToChill;
baseRecipe.maltose = 0.8 * baseRecipe.grain;
baseRecipe.sediment = baseRecipe.wortToFerment - baseRecipe.gallons;
baseRecipe.beer = baseRecipe.wortToFerment - baseRecipe.sediment;

%display calculated baseRecipe values
fprintf("Homebrew recipe calculated values:\n")
disp(baseRecipe)

%calculate simple scaled values
scaled.gallons = scaled.barrels * 31;
scaled.scaleFactor = scaled.gallons / baseRecipe.gallons;

%scale up recipe
scaled = scaleRecipe(baseRecipe, scaled);

%print scaled recipe
fprintf("Scaled Up Recipe Calculated values:\n")
disp(scaled)

