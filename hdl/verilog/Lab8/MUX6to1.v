module MUX6to1(
    input  [2:0] S,               // 3-bit select bit
    input  [2:0] A, B, C, D, E, F, // 3-bit input values
    output [2:0] out);             // 3-bit output value

    // 3-bit temporary variables
    wire [2:0] tempA, tempB, tempC, tempD;

    MUX3bit2to1 MUX0(.A(A), .B(B), .S(S[0]), .out(tempA));
    MUX3bit2to1 MUX1(.A(C), .B(D), .S(S[0]), .out(tempB));
    MUX3bit2to1 MUX2(.A(E), .B(F), .S(S[0]), .out(tempC));


    MUX3bit2to1 MUX3(.A(tempA), .B(tempB), .S(S[1]), .out(tempD));


    MUX3bit2to1 MUX5(.A(tempD), .B(tempC), .S(S[2]), .out(out));

endmodule
