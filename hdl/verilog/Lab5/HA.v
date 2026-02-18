module HA(
input A, B,
output Co, S
);
    assign S = A^B;
    assign Co = A&B;

endmodule

