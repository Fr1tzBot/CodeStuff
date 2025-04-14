clc
clear a

[a, s] = initarduino();



%add constants to workspace
constants

%prompt user to select a recipe
recipe = pickrecipe();

%Brewing Process Steps:

%Malt Mill (1:1 output)
crushedGrain = mill(recipe.grain);

%Brew Kettle / Mashing
wort = mash(a, crushedGrain);

%Lauter Tun
wort = lauter(a, crushedGrain, wort);

%Boil Kettle
wort = boil(a, recipe, wort);

%Whirlpool
wort = whirl(a,wort);

%Plate Chiller (1:1 output)
wort = chill(a,wort);

%Fermenter
beer = ferment(a, crushedGrain, recipe.yeast, wort, recipe.gallons);

%Storage
store(beer);

exit(0)

