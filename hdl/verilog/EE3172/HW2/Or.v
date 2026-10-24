module Or(
        input [31:0] inputA,
        input [31:0] inputB,
        output reg [31:0] orOut
);

assign orOut = inputA | inputB;

endmodule
