% oxygenDataParser.m: parses sample oxygen data, estimates the status of the provided astronauts, and toggles LEDs to reflect their status
% Author: Fritz Geib
% Date: 12/5/2024

% set up workspace
clc
clear all

% Load the data
[time, person1, person2] = readvars('DemoP1.xlsx');

% initialize state machines and buffers for both people
p1status = "";
p2status = "";
p1buffer = "";
p2buffer = "";

%parseplayer: returns a matrix containing two elements, first the green led pin, then the red led pin
%@param player: the player number (1 or 2)
function pins = parseplayer(player)
    if player == 1
        pins = ["D8", "D10"];
    elseif player == 2
        pins = ["D2", "D4"];
    end
end

%statustoled: toggle the appropriate pins on the arduino based on the provided status
%@param a: the arduino object
%@param status: the status of the player
%@param player: the player number (1 or 2)
%@see parseplayer
function statustoled(a, status, player)
    pins = parseplayer(player);
    if status == "eva"
        a.writeDigitalPin(pins(1), 1)
        a.writeDigitalPin(pins(2), 0)
    else
        a.writeDigitalPin(pins(1), 0)
        a.writeDigitalPin(pins(2), 1)
    end
end

%printstatus: prints the status of the person and triggers an led update if the status has changed
%@param a: the arduino object
%@param person: the person number (1 or 2)
%@param status: the current status of the person
%@param buffer: the previous status of the person
%@param t: the current time
function printstatus(a, person, status, buffer, t)
    if status ~= buffer
        if status == "awake" && buffer == "sleep"
            % fprintf("Person %d woke up at %d\n", person, t);
        elseif status == "sleep" && buffer == "awake"
            % fprintf("Person %d fell asleep at %d\n", person, t);
        elseif status == "eva" && buffer == "awake"
            fprintf("Person %d went on an EVA at %d\n", person, t);
            statustoled(a, status, person)
        elseif status == "awake" && buffer == "eva"
            fprintf("Person %d returned from EVA at %d\n", person, t);
            statustoled(a, status, person)
        elseif status == "" || buffer == ""
            % Do nothing
        else
            fprintf("Person %d transitioned from %s to %s at %d\n", person, buffer, status, t);
        end
    end
end

% Constants
UPPER_THRESHOLD = 0.55; % o2 value above this is an EVA
LOWER_THRESHOLD = 0.38; % o2 value below this is sleeping
GROUND_PINS = ["D3", "D5", "D9", "D11"]; % pins to ground the LEDs

% Initialize the arduino
a = arduino();

% Ground the LEDs
for i=1:length(GROUND_PINS)
    a.writeDigitalPin(GROUND_PINS(i), 0)
end

% removed plotting code
hold on
plot(time, person1, 'r');
plot(time, person2, 'b');
yline(LOWER_THRESHOLD)
yline(UPPER_THRESHOLD)
xlabel('Time (s)');
ylabel('Oxygen Level');
title('Oxygen Levels Over Time');
legend('Person 1', 'Person 2');
hold off

%initialize leds
statustoled(a, p1status, 1)
statustoled(a, p2status, 2)

for i = 1:length(time)
    % Get the time
    t = time(i);

    p1buffer = p1status;
    p2buffer = p2status;

    % Get the status of person 1
    if person1(i) >= UPPER_THRESHOLD
        p1status = "eva";
    elseif person1(i) <= LOWER_THRESHOLD
        p1status = "sleep";
    else
        p1status = "awake";
    end

    % Get the status of person 2
    if person2(i) >= UPPER_THRESHOLD
        p2status = "eva";
    elseif person2(i) <= LOWER_THRESHOLD
        p2status = "sleep";
    else
        p2status = "awake";
    end

    % Print the status of both people
    printstatus(a, 1, p1status, p1buffer, t)
    printstatus(a, 2, p2status, p2buffer, t)

    % Pause for a moment to simulate real-time data
    pause(0.02)
end
