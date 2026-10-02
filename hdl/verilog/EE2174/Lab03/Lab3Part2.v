/*
Author: Fritz Geib
Program Name: Lab3Part2 
**/

module Lab3Part2(
input [3:0] SW,
output [2:0] LEDR);

	wire a, b;
	
	and(a, SW[0], SW[1]);
	and(b, SW[2], SW[3]);
	or(LEDR[0], a, b);
	
endmodule