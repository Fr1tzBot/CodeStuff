library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity tb_halfAdder is
end tb_halfAdder;

architecture behavior of tb_halfAdder is
    signal A : STD_LOGIC := '0';
    signal B : STD_LOGIC := '0';
    signal SUM : STD_LOGIC;
    signal CARRY : STD_LOGIC;

    component halfAdder
        Port (
            A : in STD_LOGIC;
            B : in STD_LOGIC;
            SUM : out STD_LOGIC;
            CARRY : out STD_LOGIC
        );
    end component;

begin
    UUT: halfAdder
        port map (
            A => A,
            B => B,
            SUM => SUM,
            CARRY => CARRY
        );

    stim_proc: process
    begin
        A <= '0'; B <= '0';
        wait for 10 ns;

        A <= '0'; B <= '1';
        wait for 10 ns;

        A <= '1'; B <= '0';
        wait for 10 ns;

        A <= '1'; B <= '1';
        wait for 10 ns;

        wait;
    end process;
end behavior;

