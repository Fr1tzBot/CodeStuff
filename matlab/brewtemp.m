clc
clear

inittemp = 45.7; %starting temp in F
temp = inittemp; %initialize temp to specified start temp
count = 0;

while temp > 32 % each loop is one minute
    temp = temp - 0.2; %decrease temp by 2 degrees f per minute
    count = count + 1; %increment count by 1 every second
end

fprintf("took %d minutes to cool from %.1f˚F to %.1f˚F\n", count, inittemp, temp)


%bonus no loop

fprintf("took %d minutes to cool from %.1f˚F to %.1f˚F\n", ceil((inittemp-32)/0.2), inittemp, 32-mod(inittemp-32, 0.2))
