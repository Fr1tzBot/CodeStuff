module And(
    input [31:0] inputA,
    input [31:0] inputB,
    output reg [31:0] andOut
);

assign andOut = inputA & inputB;

endmodule
