module Lab8Part2(
input [3:0]SW,
output wire  [6:0]HEX0);

    HelloDecoder helo(.num (SW), .display (HEX0));
endmodule