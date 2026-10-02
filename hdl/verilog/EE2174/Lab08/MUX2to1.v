module MUX2to1 (
input A, B, S,
output out);
    assign out = (~S&A)|(S&B);
endmodule
