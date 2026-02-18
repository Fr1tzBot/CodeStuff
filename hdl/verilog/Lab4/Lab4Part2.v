module Lab4Part2(
input[3:0]SW,
output wire [6:0] HEX0);
    hex7seg instanceName(.num (SW), .display (HEX0));
endmodule
