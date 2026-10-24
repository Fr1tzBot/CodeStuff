{ pkgs ? import <nixpkgs> { } }:

pkgs.mkShell {
  packages = with pkgs; [
    # simulation
    iverilog        # Icarus Verilog
    # verilator       # fast linting + C++ simulation
    gtkwave         # waveform viewer
    surfer          # modern waveform viewer (optional)

    # synthesis / FPGA (open source flow)
    # yosys
    # nextpnr
    # icestorm        # iCE40 bitstream tools
    # trellis         # ECP5 bitstream tools
    # openfpgaloader

    # editor / lint / format tooling
    # verible         # formatter, linter, language server

    # testing + build
    gnumake
    gcc
  ];

  shellHook = ''
    echo "Verilog env ready: make sim | make wave | make lint | make synth"
  '';
}
