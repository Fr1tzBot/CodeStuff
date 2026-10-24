module Adder(
    input [31:0] inputA,
    input [31:0] inputB,
    output reg [31:0] addOut
);

assign addOut = inputA + inputB;

endmodule
