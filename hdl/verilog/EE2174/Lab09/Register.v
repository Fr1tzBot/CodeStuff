module Register(
	input clk, reset,
	input [7:0] D,
	output reg [7:0] Q
);

	always@(posedge clk or negedge reset)
	begin
		if (reset == 0)
			Q <= 0;
		else
			Q <= D;
	end
	
endmodule
