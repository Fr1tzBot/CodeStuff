% NAME
% TEAM AND SECTION NUMBER
% leap week 10 
% students will be asked to determine how many pieces of candy that they
% give out to trick or treaters on halloween.
% 10/27/2024

%% housekeeping
clear
clc
close all

%% initialize variables
trickortreaters = randi(3,1,50) ; %number of trick or treaters every time there is a knock at the door
candydepletion = randi(3,1,50) ; % how many pieces of candy each kid takes
candyamount = 100 ; 
candybags = 2 ; 


%% create the for loop
for i=1:trickortreaters
    if 
        % calculate candy loss
        candyloss = trickortreaters * candydepletion;
         % calculate new candy amount 
        candyamount = candyamount - candyloss
            % record total candy 
        
    elseif 
           % calculate candy bag loss 

             % calculate candy amount taking into consideration the new bag and loss

                % record total candy 

    else 
           % calculate candy bag loss  

              % calculate candy amount taking into consideration the new bag and loss

                 % record total candy 


%% display results to the user

% display how many times the door was knocked on using sprintf

% display how much candy was left over using sprintf 

%% create a vector of how many times the door was knocked on 


%% Plot data

% plot door knocks vs candy
