module Mux2to1(
        input [31:0] inputA,
        input [31:0] inputB,
        input select,
        output reg [31:0] muxOut
);

assign muxOut = select ? inputA : inputB;

endmodule
