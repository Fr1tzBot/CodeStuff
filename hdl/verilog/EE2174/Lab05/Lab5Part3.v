module Lab5Part3(
input[7:0] SW,
output wire [6:0] HEX0,
output wire [6:0] HEX1,
output wire [4:0] LEDR);

wire [3:0] S;
wire [3:0] C;

FA fa0(.A(SW[0]), .B(SW[4]), .Cin(0), .S(S[0]), .Co(C[0]));
FA fa1(.A(SW[1]), .B(SW[5]), .Cin(C[0]), .S(S[1]), .Co(C[1]));
FA fa2(.A(SW[2]), .B(SW[6]), .Cin(C[1]), .S(S[2]), .Co(C[2]));
FA fa3(.A(SW[3]), .B(SW[7]), .Cin(C[2]), .S(S[3]), .Co(C[3]));

//assign S[4:4] = C[3:3];
assign LEDR[3:0] = S[3:0];
assign LEDR[4] = C[3];
hex7seg hex0(.num (S[3:0]), .display (HEX0));
hex7seg hex1(.num (C[3]), .display (HEX1));

endmodule
