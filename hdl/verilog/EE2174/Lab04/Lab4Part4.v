module Lab4Part4(
input CLOCK_50,
output wire [6:0] HEX0);

    reg [25:0] count;
	 reg [7:0] heex;
    parameter X = 25000000;
	 hex7seg blah(.num (heex), .display (HEX0));

    always @(posedge CLOCK_50)
    begin
        count = count + 1;
        if (count == X)
        begin
            count = 0;
				heex = heex + 1;
        end
    end
endmodule
