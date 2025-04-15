clc
clear all

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
pump(a, true)
pause(1)
pump(a, false)

%Lauter Tun
wort = lauter(a, crushedGrain, wort);
pump(a, true)
pause(1)
pump(a, false)

%Boil Kettle
wort = boil(a, recipe, wort);
pump(a, true)
pause(1)
pump(a, false)

%Whirlpool
wort = whirl(a,wort);
pump(a, true)
pause(1)
pump(a, false)

%Plate Chiller (1:1 output)
wort = chill(a,wort);
pump(a, true)
pause(1)
pump(a, false)

%Fermenter
beer = ferment(a, recipe, wort);
pump(a, true)
pause(1)
pump(a, false)

%Storage
store(beer);

%exit(0)

