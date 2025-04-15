%returns the yeast growth rate in lbs/gal-hr
function yeastRate = getYeastRate(consts, yeast)
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

    dx = mu_max * (yeastYield * sugarI + yeastI - yeast) * yeast;
    dt = saturationConc * yeastYield + yeastYield * sugarI + yeastI - yeast;

    yeastRate = dx / dt;
end

