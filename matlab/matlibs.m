% matlib.c: mad libs in matlab
% author: Fritz Geib
% date: 10/14/2024
clc

length = input("How many sentences do you want to run for?");
output = "";

for i = 1:length
    name = input("Enter a name: ", "s");
    adj =  input("Enter an adjective: ", "s");
    noun = input("Enter a noun: ", "s");
    verb = input("Enter a verb: ", "s");
    adv =  input("Enter an adverb: ", "s");

    output = append(output, sprintf("%s is a %s %s who likes to %s %s.\n", name,  adj,  noun,  verb,  adv));
end

disp(output)

