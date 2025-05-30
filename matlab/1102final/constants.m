%Constants.m
%contains constant values including brew recipes and pin maps

%Recipe for Spotted Clown (New Glarus Spotted Cow clone)
recipe1.gallons = 5.5;
recipe1.grain = 12; %lbs of grain
recipe1.yeast = 0.0254; %lbs
recipe1.hops.oz = [0.5, 0.5, 0.5]; %oz for each hop
recipe1.hops.aa = [6.7, 5.8, 5.2]; %percent of hop weight that is alpha acid
recipe1.hops.bt = [60, 20, 5]; %minutes of boil time
recipe1.hops.names = ["cascade", "german select", "willamette"];

%Recipe for New Glarus Fat Squirrel Clone
recipe2.gallons = 5.5;
recipe2.grain = 10; %lbs of grain
recipe2.yeast = 0.0254;
recipe2.hops.oz = [0.5, 1]; %oz for each hop
recipe2.hops.aa = [14, 4]; %percent of hop weight that is alpha acid
recipe2.hops.bt = [0, 10]; %minutes of boil time
recipe2.hops.names = ["magnum", "saaz"];

%Pin Maps:
hwmap.leds.mash    = 'D2';
hwmap.leds.lauter  = 'D3';
hwmap.leds.boil    = 'D4';
hwmap.leds.whirl   = 'D5';
hwmap.leds.chill   = 'D6';
hwmap.leds.ferment = 'D7';
hwmap.gaugeServo   = 'D9';
hwmap.pump.pin1    = 'D11'; %these two are also wired to indicator leds
hwmap.pump.pin2    = 'D12';
hwmap.thermistor   = 'A0';

%Pump Invert:
pumpInvert = true;
