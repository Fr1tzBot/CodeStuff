module Lab4Part1(
input CLOCK_50,
output reg [9:0] LEDR);

    reg [25:0] count;
    parameter X = 25000000;

    always @(posedge CLOCK_50)
    begin
        count = count + 1;
        if (count == X)
        begin
            count = 0;
            LEDR = LEDR + 1;
        end
    end
endmodule
