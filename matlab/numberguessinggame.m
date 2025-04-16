% Fritz

% LEAP 1102 Spring for loop exercise

%3/7/25



clear

clc



number = randi(100,1);



disp('you have 10 tries to guess the number')

a = arduino();

guess = input('guess the value 1-100: ');

count = 0;

RED = 'D3';
YELLOW = 'D5';
WHITE = 'D6';
GREEN = 'D2';

for i=1:11

    if number == guess

        disp('Congrats you win!')

        fprintf('it took you %0.0f tries to guess \n', count)

        %turn on green light
        a.writeDigitalPin(GREEN, 1);

        break

    elseif abs(guess - number) <= 5

        disp('red hot, so close!')

        %turn on red light
        a.writeDigitalPin(YELLOW, 1);

        guess = input('guess again: ');

        count = count+1;

    elseif number < guess

        disp('guess lower')

        %turn on red light
        a.writeDigitalPin(RED, 1);

        guess = input('guess again: ');

        count = count+1;

    elseif number > guess

        disp('guess higher')

        %turn on green light
        a.writeDigitalPin(WHITE, 1);

        guess = input('guess again: ') ;

        count = count+1;

    else

        disp('you lose!')

        fprintf('the number was %0.0f \n', number)

        %blink red light 5 times
        for i=1:5

            a.writeDigitalPin(RED, 1);

            pause(0.5);

            a.writeDigitalPin(RED, 0);

            pause(0.5);
        end

    end
    pause(1);
    a.writeDigitalPin(RED, 0);
    a.writeDigitalPin(YELLOW, 0);
    a.writeDigitalPin(WHITE, 0);
    a.writeDigitalPin(GREEN, 0);

end



if number ~= guess

    disp('you lose :(')

    fprintf('the number was %0.0f \n', number)

    %blink red light 5 times
    for i=1:5

        a.writeDigitalPin(RED, 1);

        pause(0.5);

        a.writeDigitalPin(RED, 0);

        pause(0.5);
    end

else

    disp('Congrats you win!')

    fprintf('it took you %0.0f tries to guess \n', count)

end

