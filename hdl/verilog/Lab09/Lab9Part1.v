module Lab9Part1 (
	input[1:0] SW,
	output[0:0] LEDR
);

	GatedDLatch la1(.clk(SW[1]), .D(SW[0]), .Q(LEDR[0]));
	
endmodule