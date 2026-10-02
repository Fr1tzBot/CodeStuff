module Lab9Part2 (
	input [1:0] SW,
	input [0:0] KEY,
	output [7:0] LEDR
);

	Nonblock nb(.clk(SW[0]), .reset(KEY[0]), .E(SW[1]), .Q(LEDR[7:0]));

endmodule
