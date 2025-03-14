% make a function with cost per gallon, efficiency, and distance as inputs

function [cost] = gasCost(pergal, eff, dist)
    cost = (dist / eff) * pergal;
end

