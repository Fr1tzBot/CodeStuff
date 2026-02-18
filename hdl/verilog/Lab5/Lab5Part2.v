module Lab5Part2(
input[2:0] SW,
output[1:0] LEDR);

FA fa(.A(SW[1:1]), .B(SW[2:2]), .Cin(SW[0:0]), .S(LEDR[0:0]), .Co(LEDR[1:1]));

endmodule
