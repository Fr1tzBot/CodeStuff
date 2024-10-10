% help me im trapped in here they havent fed me in days

clc

% recipe
bread = 4;
patty = 1;
cheese = 2;
pickle = 4;

% amount per package
breadLoaf = 16;
beefPound = 4;
cheesePack = 8;
pickleJar = 64;


% prompt for purchased ingredients
breadCount = input("How many Loafs of bread did you buy? ") * breadLoaf;
pattyCount = input("How many Pounds of beef did you buy? ") * beefPound;
cheeseCount = input("How many packs of cheese did you buy? ") * cheesePack;
jarCount = input("How many jars of pickles did you buy? ") * pickleJar;

% calculate how many recipes can be made
recipes = [breadCount/bread pattyCount/patty cheeseCount/cheese jarCount/pickle];

% display the 
disp(min(recipes))
