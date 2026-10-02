module Lab9Part3(
	input [7:0] SW,
	input [1:0] KEY,
	output wire [6:0] HEX0,
	output wire [6:0] HEX1,
	output wire [6:0] HEX4,
	output wire [6:0] HEX5
);

		wire [7:0] Q;

		Register reg1(.clk(KEY[1]), .reset(KEY[0]), .D(SW), .Q(Q));
		
		hex7seg sw1(.num(SW[3:0]), .display(HEX0));
		hex7seg sw2(.num(SW[7:4]), .display(HEX1));
		
		hex7seg val1(.num(Q[3:0]), .display(HEX4));
		hex7seg val2(.num(Q[7:4]), .display(HEX5));

endmodule
