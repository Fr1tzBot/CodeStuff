// Hello decoder
module HelloDecoder(
    input  [2:0] num,           // Three bit input that can take a value between 0 and 7
    output reg [6:0] display);  // Output intended to go to 7-segment display i.e. HEX0

    always@(num)
    begin
        case(num)
            3'd0: display = 7'b0001001; // Display H
            3'd1: display = 7'b0000110; // Display E
            3'd2: display = 7'b1000111; // Display L
            3'd3: display = 7'b1000000; // Display O
            default: display = 7'b1111111;
        endcase
    end

endmodule
