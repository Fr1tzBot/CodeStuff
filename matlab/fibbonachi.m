clc
clear

n = 20;

fib = zeros(1,n);

for i = 1:n
    if i == 1
        fib(i) = 0;
    elseif i == 2
        fib(i) = 1;
    else
        fib(i) = fib(i-1) + fib(i-2);
    end
end

fib
