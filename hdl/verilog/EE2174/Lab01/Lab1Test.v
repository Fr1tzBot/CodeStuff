/*
Author: Fritz Geib
Program Name: Lab1Test
Creation Date: 1/13/2026
Last Updated: 1/13/2026 4:30pm
Function: test Lab1Part1 In Bench Waveform sim
Method: simple boolean switch inputs to view possible outputs
*/

module Lab1Test(
output [2:0] f);

	reg [4:0] SW;
	
	Lab1Part1 DUT(.SW (SW), .LEDR (f));
	
	initial
	begin
	
		SW[0] = 1'b0; SW[1] = 1'b0;
		SW[2] = 1'b0; SW[3] = 1'b0;
		SW[4] = 1'b0;
		
		#10;
		
		SW[0] = 1'b1;
		SW[2] = 1'b1;
		SW[4] = 1'b1;
		
		#10;
		
		SW[1] = 1'b1;
		SW[3] = 1'b1;
		SW[4] = 1'b0;
		
		#10;
	end
endmodule
