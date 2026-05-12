use std::io::{stdout, Stdout};
use termion::raw::{IntoRawMode, RawTerminal};
use crate::Board;

const GRID_WIDTH: u16 = 32; //4 * (5+2) + (4+1)
const GRID_HEIGHT: u16 = 17;
const CELL_HEIGHT: usize = 3;
const CELL_WIDTH: usize = 7;
const BLOCK_CHAR: char = '#';
const CELL_CORDS: [[(u16, u16); 4]; 4] = [
    [(5, 3), (13, 3), (21, 3), (29, 3)],
    [(5, 7), (13, 7), (21, 7), (29, 7)],
    [(5, 11), (13, 11), (21, 11), (29, 11)],
    [(5, 15), (13, 15), (21, 15), (29, 15)]
];

pub struct Renderer {
    _term: RawTerminal<Stdout>,
}

impl Renderer {

    pub fn new() -> Self {
        Self { _term: stdout().into_raw_mode().unwrap()}
    }

    pub fn clear_screen(&self) {
        print!("\x1b[2J\x1b[H");
    }


    fn move_to(&self, x: u16, y: u16) {
        print!("\x1b[{};{}H", y, x);
    }

    pub fn render(&self, board: &Board) {
        self.clear_screen();
        //Paint horizontal bars ([1, 5, 9, 13, 17])
        for j in (1..=GRID_HEIGHT).step_by(CELL_HEIGHT+1) {
            self.move_to(1, j);
            for _i in 0..=GRID_WIDTH {
                print!("{}", BLOCK_CHAR);
            }
        }

        //Paint vertical bars [1, 9, 17, 25, 33], stopping before bottom as the bottom line is already full
        for i in  (1..=(GRID_WIDTH+1)).step_by(CELL_WIDTH+1) {
            for j in 1..GRID_HEIGHT {
                self.move_to(i, j);
                print!("{}", BLOCK_CHAR);
            }
        }

        for (y, row) in board.data.iter().enumerate() {
            for (x, num) in row.iter().enumerate() {
                let offset_x = if *num == 0 {0} else {
                    match num.ilog10() {
                        2..=4 => 1,
                        5 => 2,
                        _ => 0
                    }
                };
                self.move_to(CELL_CORDS[y][x].0 - offset_x, CELL_CORDS[y][x].1);
                print!("{}", num);
            }
        }
        print!("\r\n\n\n");
    }
}

