/*
Author: Fritz Geib
Program Name: Lab0
Creation Date: 1-6-2026
Date Last Updated: 5:00pm
Function: assigns each switch to a corresponding red LED
Method: using prewritten instructions
Inputs: switches 9-0
Outputs: LEDR 9-0
Comments: N/A
*/


module Lab0(
input[9:0] SW,
output [9:0] LEDR);

	assign LEDR = SW;
	
endmodule