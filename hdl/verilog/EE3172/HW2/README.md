# Verilog dev environment (NixOS, no flakes)

## Usage
    nix-shell            # drops you into the environment (uses shell.nix)
    make sim             # compile + run testbench (iverilog)
    make wave            # open waveform in GTKWave
    make lint            # verilator + verible
    make synth           # yosys synthesis stats

Use another module: `make sim TOP=alu` (expects `tb/tb_alu.v`).

Optional: with direnv + nix-direnv, `direnv allow` loads the shell automatically (`.envrc`).

## System-wide alternative
Instead of a shell, add the packages in `/etc/nixos/configuration.nix`:

    environment.systemPackages = with pkgs; [
      iverilog verilator gtkwave yosys nextpnr icestorm verible gnumake
      (python3.withPackages (ps: [ ps.cocotb ps.pytest ]))
    ];

then `sudo nixos-rebuild switch`.
