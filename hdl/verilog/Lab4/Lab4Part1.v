module Lab4Part1(
input CLOCK_50,
output reg [9:0] LEDR);

    reg [16:0] count;
    parameter X = 50;

    always @(poseedge CLOCK_50)
    begin
        count = count + 1;
        if (count == X)
        begin
            count = 0;
            LEDR = LEDR + 1;
        end
    end
endmodule
