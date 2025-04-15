%returns the yeast growth rate in lbs/gal-hr
function yeastRate = getYeastRate(consts, yeast, sugar)
    %\mu_max = consts.maxGrowth
    %Y_{x/s} = consts.yeastI / consts.sugarI?
    %S_0 = consts.sugarI
    %X_0 = consts.yeastI
    %X = yeast
    %K_s = consts.saturationConc
    mu_max = consts.maxGrowth;
    yeastYield = consts.yeastYield;
    sugarI = consts.sugarI;
    yeastI = consts.yeastI;
    saturationConc = consts.saturationConc;

    dx = mu_max * (yeastYield * sugar + yeastI - yeast) * yeast;
    dt = saturationConc * yeastYield + yeastYield * sugar + yeastI - yeast;

    yeastRate = dx / dt;
end

