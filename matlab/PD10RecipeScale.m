clc
clear all

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
disp(baseRecipe)
disp(scaled)

