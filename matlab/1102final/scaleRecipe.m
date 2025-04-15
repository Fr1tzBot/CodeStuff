% scaleRecipe: return a scaled up version of a given recipe
function scaledRecipe = scaleRecipe(baseRecipe, barrels)
    scaleFactor = (barrels * 31)/baseRecipe.gallons;
    fields = fieldnames(baseRecipe); % pull struct fields from baseRecipe struct
    for i = 1:numel(fields)
        field = fields{i}; %assign "field" to the selected field
        value = baseRecipe.(field); %assign "value" to the corresponding value
        if ~strcmp(field, "hops") %skip values that don't need to be scaled
            scaledRecipe.(field) = value * scaleFactor; %assign scaled values to scaledRecipe
        else
            scaledRecipe.hops = baseRecipe.hops;
            scaledRecipe.hops.oz = baseRecipe.hops.oz * scaleFactor;
        end
    end
end
