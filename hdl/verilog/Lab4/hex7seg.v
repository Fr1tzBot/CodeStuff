module hex7seg(
input [3:0]num,
output reg [6:0]display);

    always @(num)
        case (num)
            4'h0:display=7'b1000000;
            4'h1:display=7'b1111001;
            4'h2:display=7'b1000000;
            4'h3:display=7'b1000000;
            4'h4:display=7'b1000000;
            4'h5:display=7'b1000000;
            4'h6:display=7'b1000000;
            4'h7:display=7'b1000000;
            4'h8:display=7'b1000000;
            4'h9:display=7'b1000000;
            4'hA:display=7'b1000000;
            4'hB:display=7'b1000000;
            4'hC:display=7'b1000000;
            4'hD:display=7'b1000000;
            4'hE:display=7'b1000000;
            4'hF:display=7'b1000000;
            default:display=7'bx ;
        endcase
endmodule

module Lab4Part2(
input[3:0]SW,
output wire [6:0] HEX0);
    hex7seg instanceName(.num (SW), .display (HEX0));
endmodule
