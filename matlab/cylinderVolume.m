% Define the function to calculate the volume of a cylinder
function volume = cylinderVolume(r, h)
    % Convert radius and height to feet
    r = r / 12;
    h = h / 12;

    % Calculate the volume of the cylinder
    volume = pi * r^2 * h;
end
