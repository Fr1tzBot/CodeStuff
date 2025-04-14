function recipe = pickrecipe()
    %import constants
    constants

    %create an array with recipe options
    lines = [
        "We Currrently support the following recipes:", ...
        "(1) Spotted Clown (New Glarus Spotted Cow clone) [5.5 gallon batch]", ...
        "(2) New Glarus Fat Squirrel Clone [5.5 gallon batch]", ...
        "(3) Spotted Clown (New Glarus Spotted Cow clone) [10 bbl batch]", ...
        "(4) New Glarus Fat Squirrel Clone [10 bbl batch]\n"
    ];
    %merge array into one string and prompt user with it
    num = input(strjoin(lines, "\n"));

    %match the selection to the recipe
    switch num
        case 1
            recipe = recipe1;
        case 2
            recipe = recipe2;
        otherwise
            %exit with code 1 if input doesn't match
            exit(1)
    end
    clc
end
