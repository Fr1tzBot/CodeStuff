module Lab11Part2(
	input [0:0] SW,
	input [1:0] KEY,
	output [6:0] HEX0
);

	wire [3:0] hexout;
	hex7seg sevenseg(.num (hexout[3:0]+9), .display (HEX0[6:0]));
	Lab11FSM2 FSM(.reset (~KEY[1]), .clock (~KEY[0]), .transition (SW[0]), .hexout (hexout[3:0]));

endmodule