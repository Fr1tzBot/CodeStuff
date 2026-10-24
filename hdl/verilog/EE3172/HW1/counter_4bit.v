module counter_4bit (
    input  wire       clk,    // clock
    input  wire       inc,    // increment enable
    input  wire       rst_n,  // asynchronous, active-low reset
    output reg  [3:0] count   // current count value
);

    // Initialize to zero (simulation / FPGA power-up value)
    initial count = 4'b0000;

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n)
            count <= 4'b0000;        // async reset to zero
        else if (inc)
            count <= count + 4'b1;   // increment on rising edge when inc is high
    end

endmodule

