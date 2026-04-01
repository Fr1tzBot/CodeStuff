// Standard 2174 7-segment display module that takes a 4 bit number and sends
// a corrisponding signal to a 7-segment display to show the hex value of the
// input 4 bit number (0->F)
module hex7seg(
input [3:0]num,             // four bit input number that can take a value between 0 and 16
output reg [6:0]display);   //Output intended to go to a 7-segment display i.e. HEX0

	 always @(num)
        case (num)
                4'h0:display=7'b1000000; //Displays 0
				4'h1:display=7'b1111001; //Displays 1    
				4'h2:display=7'b0100100; //Displays 2    
				4'h3:display=7'b0110000; //Displays 3     	//    0     --
				4'h4:display=7'b0011001; //Displays 4    	//  5   1  |  |
				4'h5:display=7'b0010010; //Displays 5         	//    6     --
				4'h6:display=7'b0000010; //Displays 6           //  4   2  |  |
				4'h7:display=7'b1111000; //Displays 7           //    3     --
				4'h8:display=7'b0000000; //Displays 8         	
				4'h9:display=7'b0011000; //Displays 9
				4'hA:display=7'b0001000; //Displays A (10)
				4'hb:display=7'b0000011; //Displays b (11)
				4'hC:display=7'b1000110; //Displays C (12)
				4'hd:display=7'b0100001; //Displays d (13)
				4'hE:display=7'b0000110; //Displays E (14)
				4'hF:display=7'b0001110; //Displays F (15)
            default:display=7'bx ; //default case, dosent care what it displays
        endcase
endmodule
