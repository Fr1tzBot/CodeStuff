function recipe = pickrecipe()
    %import constants
    constants

    %create an array with recipe options
    lines = [
        "We Currrently support the following recipes:", ...
        "(1) Spotted Clown [10 bbl batch]", ...
        "(2) Fat Squirrel [10 bbl batch]", ...
        "(3) Spotted Clown [custom batch]", ...
        "(4) Fat Squirrel [custom batch]", ...
        "(5) Custom Recipe [custom batch]\n"
    ];
    %merge array into one string and prompt user with it
    num = input(strjoin(lines, "\n"));

    %match the selection to the recipe
    switch num
        case 1
            recipe = scaleRecipe(recipe1, 10.0);
        case 2
            recipe = scaleRecipe(recipe2, 10.0);
        case 3
            recipe = scaleRecipe(recipe1, input("What Sized Batch would you like? "));
        case 4
            recipe = scaleRecipe(recipe2, input("What Sized Batch would you like? "));
        case 5
            recipe.gallons = input("How many gallons in your recipe? ");
            recipe.grain = input("How many lbs of grain in your recipe? ");
            recipe.yeast = input("How many lbs of yeast in your recipe? ");
            for i = 1:input("How many hops in your recipe? ")
                recipe.hops.names(i) = input(sprintf("What is the name of hop %d? ", i));
                recipe.hops.oz(i) = input(sprintf("How many ounces of %s? ", recipe.hops.names(i)));
                recipe.hops.aa(i) = input(sprintf("What is the alpha acid of %s? ", recipe.hops.names(i)));
                recipe.hops.bt(i) = input(sprintf("What boil time for %s? ", recipe.hops.names(i)));
            end
        otherwise
            %exit with code 1 if input doesn't match
            exit(1)
    end
    clc
end
