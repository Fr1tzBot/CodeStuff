clc
clear all

a = arduino();

% define pins

PINS.ALARM       = 'D2';
PINS.ESTOP       = 'D3';
PINS.HLT_LED     = 'D4';
PINS.HLT_DSP     = 'D5';
PINS.MASH_DSP    = 'D6';
PINS.HLT_HEAT    = 'A0';
PINS.BOIL_HEAT   = 'A1';
PINS.MASH_HEAT   = 'A2';
PINS.CHILLER     = 'D7';
PINS.PUMP_1      = 'D8';
PINS.PUMP_2      = 'D9';
PINS.WORT        = 'D10';
PINS.FERM_DSP    = 'D11';
PINS.FERM_SWITCH = 'D12';

% configure pins
a.configurePin(PINS.ALARM, 'DigitalInput');
a.configurePin(PINS.ESTOP, 'DigitalInput');
a.configurePin(PINS.HLT_LED, 'DigitalOutput');
a.configurePin(PINS.HLT_DSP, 'DigitalOutput');
a.configurePin(PINS.MASH_DSP, 'DigitalOutput');
a.configurePin(PINS.HLT_HEAT, 'AnalogInput');
a.configurePin(PINS.BOIL_HEAT, 'AnalogInput');
a.configurePin(PINS.MASH_HEAT, 'AnalogInput');
a.configurePin(PINS.CHILLER, 'DigitalInput');
a.configurePin(PINS.PUMP_1, 'DigitalInput');
a.configurePin(PINS.PUMP_2, 'DigitalInput');
a.configurePin(PINS.WORT, 'DigitalInput');
a.configurePin(PINS.FERM_DSP, 'DigitalOutput');
a.configurePin(PINS.FERM_SWITCH, 'DigitalInput');

inputs = zeros(1, 14);
simstate = 0; % placeholder for simulation state struct

function input = readPins(a)
    input = zeros(1, 14);
    fields = fieldnames(PINS);
    for i = 1:numel(fields)
        field = fields{i};
        value = PINS.(field);
        if value(1) == 'D'
            input(i) = a.readDigitalPin(value);
        elseif value(1) == 'A'
            input(i) = a.readAnalogPin(value);
        end
    end
end

function simulate(a, inputs, simstate)
    disp("NOT IMPLEMENTED");
end

while true
    input = readPins(a);
    % Check for emergency stop
    if inputs(2) == 1
        disp('Emergency stop activated!');
        % Add code to handle emergency stop
        break;
    end

    simstate = simulate(a, inputs, simstate);
end

