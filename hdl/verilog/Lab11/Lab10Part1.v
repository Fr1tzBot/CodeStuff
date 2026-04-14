module Lab10Part1(
input clk,
input [7:0] A,
output reg [7:0] out1,
output reg [7:0] out2);

    // Non-blocking approach
    always@(posedge clk)
    begin

        out1 <= A;
        out2 <= out1;

    end

endmodule

