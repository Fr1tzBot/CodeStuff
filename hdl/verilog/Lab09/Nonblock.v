module Nonblock(
	input clk, reset, E,
	output reg [7:0] Q
);

	always@(posedge clk or negedge reset)
	begin
		if (reset == 0)
			Q <= 0;
		else if (E)
			Q <= Q + 1;
	end
	
endmodule
