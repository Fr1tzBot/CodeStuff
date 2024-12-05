clc
clear all

% Load the data
[time, person1, person2] = readvars('DemoP1.xlsx');

p1status = "";
p2status = "";
p1buffer = "";
p2buffer = "";

function pins = parseplayer(player)
    if player == 1
        pins = ["D8", "D10"];
    elseif player == 2
        pins = ["D2", "D4"];
    end
end

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

UPPER_THRESHOLD = 0.55;
LOWER_THRESHOLD = 0.38;
GROUND_PINS = ["D3", "D5", "D9", "D11"];

a = arduino();
for i=1:length(GROUND_PINS)
    a.writeDigitalPin(GROUND_PINS(i), 0)
end

% hold on
% plot(time, person1, 'r');
% plot(time, person2, 'b');
% yline(LOWER_THRESHOLD)
% yline(UPPER_THRESHOLD)
% xlabel('Time (s)');
% ylabel('Oxygen Level');
% title('Oxygen Levels Over Time');
% legend('Person 1', 'Person 2');
% hold off

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

    printstatus(a, 1, p1status, p1buffer, t)
    printstatus(a, 2, p2status, p2buffer, t)

    pause(0.02)
end
