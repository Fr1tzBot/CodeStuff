% darts.m
% Author: Fritz Geib
% Date: 12/5/2024
% Email: ftgeib@mtu.edu

function [x] = dartplotinput(i,m,o)
%circle_gen(r) Generate x and y points for a circle of given radius r
%   This function generates x,y location pairs for a complete
%   circle of radius r = i, m, and o with a center at the origin. Function is unitless.
%   i stands for inner ring, m stands for middle ring, o stands for outer ring

% equation to create x-coordinates is x = r * sin(theta)
% equation to create y-coordinates is y = r * cos(theta)
theta = 0:pi/50:2*pi; % theta is a vector variable that consists of theta values
                      % from 0 to 2pi radians in increments of pi/50
% coordinates for bullseye
bull_x = i*cos(theta);
bull_y = i*sin(theta);
% coordinates for close ring
close_x = m*cos(theta);
close_y = m*sin(theta);
% coordinates for hit ring
hit_x = o*cos(theta);
hit_y = o*sin(theta);

%Plot circles
figure('Color','w')
plot(bull_x ,bull_y ,'Color','#A2142F', "LineWidth",3) % Plot Bullseye Circle Points
hold on;                  % Hold plot for more circles
plot(close_x,close_y,'Color','#77AC30', "LineWidth",3) % Plot Close Circle Points
plot(hit_x  ,hit_y  ,'Color','#0072BD',"LineWidth",3) % Plot Hit/Miss Circle Points
axis([-4 4 -4 4]);        % Set Target Boundary
title('Target Board')
grid on

%Label Circles
text(0, 0.5,'Bullseye','HorizontalAlignment','center')
text(0, 1.5,'Close','HorizontalAlignment','center')
text(0, 2.5,'Hit','HorizontalAlignment','center')
text(0, 3.5,'Miss','HorizontalAlignment','center')

end

function dist = distance(x, y)
    dist = sqrt(x^2 + y^2);
end


[P1_x, P1_y, P2_x, P2_y] = readvars("darts_game-1.xlsx");
dartplotinput(1,2,3)

plot(P1_x, P1_y, 'ro')
plot(P2_x, P2_y, 'bo')

P1_score = 0;
P2_score = 0;

for i = 1:length(P1_x)
    dist = distance(P1_x(i), P1_y(i));


    if dist <= 1
        %bullseye
        P1_score = P1_score + 4;
    elseif dist <= 2
        P1_score = P1_score + 2;
    elseif dist <= 3
        P1_score = P1_score + 1;
    end

    %if the dart missed the board entirely, subtract 1 point
    if P1_x(i) > 4 || P1_x(i) < -4 || P1_y(i) > 4 || P1_y(i) < -4
        P1_score = P1_score - 1;
    end
end

for i = 1:length(P2_x)
    dist = distance(P2_x(i), P2_y(i));


    if dist <= 1
        %bullseye
        P2_score = P2_score + 4;
    elseif dist <= 2
        P2_score = P2_score + 2;
    elseif dist <= 3
        P2_score = P2_score + 1;
    end

    %if the dart missed the board entirely, subtract 1 point
    if P2_x(i) > 4 || P2_x(i) < -4 || P2_y(i) > 4 || P2_y(i) < -4
        P2_score = P2_score - 1;
    end
end

disp("Player 1 Score: " + P1_score)
disp("Player 2 Score: " + P2_score)

if P1_score > P2_score
    disp("Player 1 Wins!")
elseif P2_score > P1_score
    disp("Player 2 Wins!")
else
    disp("It's a tie!")
end

