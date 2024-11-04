clc
clear
dig1 = "D7";
segA = "D6";
segF = "D5";
dig2 = "D4";
dig3 = "D3";
segB = "D2";
segE = "D13";
segD = "D12";
segDec = "D11";
segC = "D10";
segG = "D9";
dig4 = "D8";
dig = [dig1, dig2, dig3, dig4]; % digit array
seg = [segA, segB, segC, segD, segE, segF, segG, segDec]; %a,b,c,d,e,f,g,decimal
cache = zeros(1,13);
data = zeros(1,8);
a = arduino();
% a = arduino()
function a = sevenseg(char, dec)
    a = [0, 0, 0, 0, 0, 0, 0, 0];
    switch char
        case 0
            a = [1, 1, 1, 1, 1, 1, 0, 0];
        case 1
            a = [0, 1, 1, 0, 0, 0, 0, 0];
        case 2
            a = [1, 1, 0, 1, 1, 0, 1, 0];
        case 3
            a = [1, 1, 1, 1, 0, 0, 1, 0];
        case 4
            a = [0, 1, 1, 0, 0, 1, 1, 0];
        case 5
            a = [1, 0, 1, 1, 0, 1, 1, 0];
        case 6
            a = [1, 0, 1, 1, 1, 1, 1, 0];
        case 7
            a = [1, 1, 1, 0, 0, 0, 0, 0];
        case 8
            a = [1, 1, 1, 1, 1, 1, 1, 0];
        case 9
            a = [1, 1, 1, 0, 0, 1, 1, 0];
    end
    if dec
        a(8) = 1;
    end
end
function cache = setPin(a, cache, pin, state, force)
    index = str2double(strip(pin,"left","D"));
    if cache(index) ~= state || force
        cache(index) = state;
        a.writeDigitalPin(pin, state)
        % fprintf("Set Pin %s to %d\n", pin, state)
    end
end
inputNumber = 99;
chars = [8, 8];
count = 0;
data = zeros(2, 30);
starttime = posixtime(datetime('now'))
% for k = 1:4 % initialize all digits to high
%     cache = setPin(a, cache, dig(k), 1, false);
% end
while num2str(posixtime(datetime('now')) - starttime * 1e6) < 60
    temp=num2str((a.readVoltage("A0")))
    chars(1)=str2double(temp(1));
    chars(2)=str2double(temp(2))
    % tic
    for i = 1:length(chars)
        count = count + 1;
        data = sevenseg(chars(i), 0);
        for k = 1:4 % pull all digit pins high
            cache = setPin(a, cache, dig(k), 1, false);
        end
        for j = 1:8
            cache = setPin(a, cache, seg(j), data(j), false); % set all 8 segments to the appropriate values
        end
       
        for k = 1:4 % pull current digit pin low and force all others to high
            cache = setPin(a, cache, dig(k), k ~= i, false);
        end
        % cache = setPin(a, cache, dig(i), 0); % pull digit pin low
        % fprintf("count: %d\n", count)
    end
    % toc
    % disp(cache)
    if mod(posixtime(datetime('now')), 2) == 2
        for i=1:length(data)
            if i ~= 0
                data(i, 1) = a.readVoltage("A0");
                data(i, 2) = posixtime(datetime('now'))
            end
        end
    end
end

plot(data(1, :), data(2, :));
xlabel("Time (Seconds)")
ylabel("Temperature (fahrenheit)")