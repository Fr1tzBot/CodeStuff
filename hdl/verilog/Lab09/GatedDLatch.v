module GatedDLatch (
	input clk, D,
	output Q
);

	wire R, Rg, Sg, Qa, Qb;
	
	assign R = ~D;
	assign Sg = D & clk;
	assign Rg = R & clk;
	assign Qa = ~(Sg|Qb);
	assign Qb = ~(Rg|Qa);
	assign Q = Qa;
	
endmodule