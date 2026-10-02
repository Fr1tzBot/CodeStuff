/*
Author: Fritz Geib
Program Name: Lab3Part2 
**/

module Lab3Part3(
input [3:0] SW,
output [2:0] LEDR);

	wire a, b;
	
	nand(a, SW[0], SW[1]);
	nand(b, SW[2], SW[3]);
	nand(LEDR[1], a, b);
	
endmodule