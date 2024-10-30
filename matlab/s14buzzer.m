% ESP14AudioAlert.mlx
% Author: Fritz Geib (ftgeib@mtu.edu)
% Date: 10/15/2024

clear
a = arduino(); % Connect to Arduino board
Frequency=[523.25,0,523.25,0,523.25,0,659.25,659.25,392,392,587.33,0,587.33,659.25,587.33,523.25,493.88,440,392];
Duration =0.2*[2,1,2,1,2,1,2,1,9,3,2,1,2,1,2,1,2,1,6];

for i = 1:length(Frequency) % Start Loop, i = 1, then i = 2, then i=3, till i = length of vector Frequency = 7.
    playTone(a, 'D3', Frequency(i), Duration(i)); % On Pin D3 play the (ith number in vector Frequency) hz tone for (Duration) seconds
    pause(Duration(i)); % Wait Duration Seconds for tone to finish
end % End Loop, move to start of loop and use next i, if any are left.

