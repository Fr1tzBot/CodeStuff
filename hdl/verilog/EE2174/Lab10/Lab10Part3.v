module Lab10Part3(
    inout [5:0] ARDUINO_IO
);

    assign ARDUINO_IO[0] = ARDUINO_IO[3];
    assign ARDUINO_IO[1] = ARDUINO_IO[4];
    assign ARDUINO_IO[2] = ARDUINO_IO[5];

endmodule
