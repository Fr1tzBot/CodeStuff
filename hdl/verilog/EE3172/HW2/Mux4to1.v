module Mux4to1(
        input [31:0] inputA,
        input [31:0] inputB,
        input [31:0] inputC,
        input [31:0] inputD,
        input [1:0] select,
        output reg [31:0] muxOut
);

//Atrocious ik
assign out = (select == 2'b00) ? inputA :
             (select == 2'b01) ? inputB :
             (select == 2'b10) ? inputC :
             (select == 2'b11) ? inputD :
                              32'h00000000;

endmodule
