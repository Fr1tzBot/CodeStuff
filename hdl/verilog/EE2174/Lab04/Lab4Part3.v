module Lab4Part3(
input[7:0]SW,
output wire [6:0] HEX0,
output wire [6:0] HEX1);
    hex7seg blah(.num (SW[3:0]), .display (HEX0));
	 hex7seg instanceName(.num (SW[7:4]), .display (HEX1));
endmodule
