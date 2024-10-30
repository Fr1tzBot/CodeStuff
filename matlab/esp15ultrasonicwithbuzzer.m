clc
clear all

a = arduino('/dev/cu.usbmodem11201', 'Uno', 'Libraries', 'Ultrasonic');
% a = arduino()
UltrasonicObj = ultrasonic(a, 'D5', 'D6')

time = [];
value = [];

tic();
for i = 1:600
    disp(i)
    time(i) = toc();
    value(i) = readDistance(UltrasonicObj)
    if readDistance(UltrasonicObj) < 0.05
        playTone(a, 'D3', 400, 0.1);
    end
    pause(0.1)
        
end

plot(time, value, "pentagram")
