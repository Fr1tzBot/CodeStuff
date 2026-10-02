module Lab5Part1(
input[2:1] SW,
output[1:0] LEDR);

HA ha(.A(SW[1:1]), .B(SW[2:2]), .S(LEDR[0:0]), .Co(LEDR[1:1]));

endmodule
