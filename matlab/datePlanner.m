function [cost] = gasCost(pergal, eff, dist)
    cost = (dist / eff) * pergal;
end

function [cost] = outfitCost(shirt, pants, shoes, tax)
    cost = (shirt + pants + shoes) * (1 + tax);
end

function [time] = time_func(dist, speed, res_time)
    time = (dist/speed) + res_time;
end

function [cost] = mealCost(app, meal, desert, drinks, tip)
    cost = (app+meal+desert+drinks) * (tip+1);
end

gas = gasCost(2.87, 15, 15.5)
outfit = outfitCost(4.99, 39.99, 9.99, 0.06)
time = time_func(15.5, 90, 2.5)
meal = mealCost(7.99, 63.54, 20, 11.98, 0.19)

total = gas+outfit+meal