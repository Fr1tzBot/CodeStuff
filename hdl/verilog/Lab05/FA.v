module FA(
input A, B, Cin,
output Co, S);

    assign S = (A&B&Cin) | (A^B^Cin);
    assign Co = (A&B) | ((A|B)&Cin);
endmodule
