% Program Name: ESPS13.m
% Program Description:
% a script file that will import the data file using readmatrix and assigns the data columns to vectors.
% Name: Fritz Geib (ftgeib@mtu.edu)
% Section: L29
% Team: 04

filename = "~/Downloads/TracePdataf13.xlsx";
data = readmatrix(filename);

% Assigning the data columns to vectors
% Variable Name 	Column
%utc 	1
%jday 	2
%flight 	4
%lat 	6
%long 	7
%alt 	8
%pres 	9
%temp 	10
%o3 	17
%co 	18
%no 	22
%no2 	23
%ethane 	108
%propane 	112
%i_butane 	114
%n_butane 	115
%PAN 	174

utc = data(4:end,1);
jday = data(4:end,2);
flight = data(4:end,4);
lat = data(4:end,6);
long = data(4:end,7);
alt = data(4:end,8);
pres = data(4:end,9);
temp = data(4:end,10);
o3 = data(4:end,17);
co = data(4:end,18);
no = data(4:end,22);
no2 = data(4:end,23);
ethane = data(4:end,108);
propane = data(4:end,112);
i_butane = data(4:end,114);
n_butane = data(4:end,115);
PAN = data(4:end,174);


