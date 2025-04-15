function recipe = pickrecipe()
    %import constants
    constants

    %create an array with recipe options
    lines = [
        "We Currrently support the following recipes:", ...
        "(1) Spotted Clown [10 bbl batch]", ...
        "(2) Fat Squirrel [10 bbl batch]", ...
        "(3) Spotted Clown [custom batch]", ...
        "(4) Fat Squirrel [custom batch]\n"
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
        otherwise
            %exit with code 1 if input doesn't match
            exit(1)
    end
    clc
end
