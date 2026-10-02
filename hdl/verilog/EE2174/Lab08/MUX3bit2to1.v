module MUX3bit2to1 (
    input  [2:0] A, B,
    input  S,
    output [2:0] out);
    assign out[0] = (~S & A[0]) | (S & B[0]);
	 assign out[1] = (~S & A[1]) | (S & B[1]);
	 assign out[2] = (~S & A[2]) | (S & B[2]);
endmodule
