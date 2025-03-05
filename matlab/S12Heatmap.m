clc
clear

avg_price=10;

prices = zeros(23,48);
for row=1:23
    for col=1:48
        if row <=9 && col >= 12 && col <=36
            prices(row, col) = 1.3*avg_price;
        elseif row >= 16 && (col <= 11 || col  >= 37)
            prices(row, col) = 0.7*avg_price;
        else
            prices(row, col) = avg_price;
        end
    end
end

% Create a heatmap
heatmap(prices);

%bonus to show how easy it is with no for loops:
% tickets = ones(23,48)*avg_price;
% tickets(1:9,12:36) = 1.3*avg_price;
% tickets(16:23,[1:11,37:48]) = 0.7*avg_price;
% heatmap(tickets, 'Colormap', jet);
