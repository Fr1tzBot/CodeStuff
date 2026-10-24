TOP      ?= counter
TB       ?= tb_$(TOP)
SRC      := $(wildcard src/*.v src/*.sv)
TBSRC    := tb/$(TB).v
BUILD    := build

.PHONY: sim wave lint synth clean

sim: $(BUILD)/$(TB).vvp
	vvp $<

$(BUILD)/$(TB).vvp: $(SRC) $(TBSRC)
	@mkdir -p $(BUILD)
	iverilog -g2012 -Wall -o $@ $(SRC) $(TBSRC)

wave: sim
	gtkwave $(BUILD)/$(TB).vcd &

lint:
	verilator --lint-only -Wall --top-module $(TOP) $(SRC)
	verible-verilog-lint $(SRC) || true

synth:
	yosys -p "read_verilog -sv $(SRC); synth -top $(TOP); stat"

clean:
	rm -rf $(BUILD)
