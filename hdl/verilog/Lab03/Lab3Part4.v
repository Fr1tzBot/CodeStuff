/*
Author: Fritz Geib
Program Name: Lab3Part2 
**/

module Lab3Part4(
input [3:0] SW,
output reg [2:0] LEDR);

	always @(*) begin
		reg a, b;
		a = ~(SW[0] & SW[1]);
		b = ~(SW[2] & SW[3]);
		LEDR[2] = ~(a & b);
	end
endmodule