/*
Author: Fritz Geib
Program Name: lab1
Creation Date: 1/13/2026
Last Updated: 1/13/2026 4:30pm
Function: emulate a couple simple logic gates and bind them to switches & leds
Method: &, |, and ! gates in line
*/

module Lab1Part1(
input [4:0] SW,
output [2:0] LEDR);

	assign LEDR[0] = SW[0] & SW[1];
	
	assign LEDR[1] = SW[2] | SW[3];
	
	assign LEDR[2] = !SW[4];
	
endmodule
