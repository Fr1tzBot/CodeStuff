library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity HalfAdder is
    Port (
        A : in STD_LOGIC;
        B : in STD_LOGIC;
        SUM : out STD_LOGIC;
        CARRY : out STD_LOGIC
    );
end HalfAdder;

architecture Behavioral of HalfAdder is
begin
    SUM <= A xor B;
    CARRY <= A and B;
end Behavioral;

