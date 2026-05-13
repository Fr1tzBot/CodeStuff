use std::io::{stdout, Stdout};
use termion::raw::{IntoRawMode, RawTerminal};
use termion::{color, cursor, clear};
use crate::Board;

const GRID_WIDTH: u16 = 32; //4 * (5+2) + (4+1)
const GRID_HEIGHT: u16 = 17;
const CELL_HEIGHT: usize = 3;
const CELL_WIDTH: usize = 7;
const BLOCK_CHAR: char = '█';
const CELL_CORDS: [[(u16, u16); 4]; 4] = [
    [(2, 3),  (10, 3),  (18, 3),  (26, 3)],
    [(2, 7),  (10, 7),  (18, 7),  (26, 7)],
    [(2, 11), (10, 11), (18, 11), (26, 11)],
    [(2, 15), (10, 15), (18, 15), (26, 15)]
];

pub struct Renderer {
    _term: RawTerminal<Stdout>,
}

impl Renderer {
    pub fn new() -> Self {
        let renderer = Self { _term: stdout().into_raw_mode().unwrap()};
        renderer.setup();
        renderer
    }

    pub fn clear_screen(&self) {
        print!("{}{}", clear::All, color::Bg(color::Reset));
    }

    fn setup(&self) {
        self.clear_screen();

        //Paint horizontal bars ([1, 5, 9, 13, 17])
        for j in (1..=GRID_HEIGHT).step_by(CELL_HEIGHT+1) {
            self.move_to(1, j);
            for _i in 0..=GRID_WIDTH {
                print!("{}{BLOCK_CHAR}{}", color::Fg(color::LightBlack), color::Fg(color::Reset));
            }
        }

        //Paint vertical bars [1, 9, 17, 25, 33], stopping before bottom as the bottom line is already full
        for i in  (1..=(GRID_WIDTH+1)).step_by(CELL_WIDTH+1) {
            for j in 1..GRID_HEIGHT {
                self.move_to(i, j);
                print!("{}{BLOCK_CHAR}{}", color::Fg(color::LightBlack), color::Fg(color::Reset));
            }
        }
    }


    fn move_to(&self, x: u16, y: u16) {
        print!("{}", cursor::Goto(x, y));
    }

    fn color_num(&self, num: &u16) -> String {
        let color: Box<dyn color::Color> = match num {
            0 => Box::new(color::Black),
            2 => Box::new(color::White),
            4 => Box::new(color::LightWhite),
            8 => Box::new(color::Cyan),
            16 => Box::new(color::LightCyan),
            32 => Box::new(color::Magenta),
            64 => Box::new(color::LightMagenta),
            128 => Box::new(color::Blue),
            256 => Box::new(color::LightBlue),
            512 => Box::new(color::Red),
            1024 => Box::new(color::LightRed),
            2048 => Box::new(color::LightYellow),
            4096 => Box::new(color::Yellow),
            8192 => Box::new(color::Green),
            16384 => Box::new(color::LightGreen),
            _ => Box::new(color::Black)
        };
        let mut output = format!("{}", color::Bg(&*color));
        if *num == 2 || *num == 4 || *num == 0 {
            output = format!("{}{}", output, color::Fg(color::Black));
        }
        output
    }

    fn write_cell(&self, x: usize, y: usize, num: &u16) {
        let num_len: u32 = if *num == 0 {1} else {num.ilog10()+1};
        let pad = match num_len {
            1 => ("   ", "   "),
            2 => ("  ", "   "),
            3 => ("  ", "  "),
            4 => ("  ", " "),
            _ => (" ", " "),
        };

        let color = self.color_num(num);
        let reset = format!("{}{}", color::Bg(color::Reset), color::Fg(color::Reset));

        self.move_to(CELL_CORDS[y][x].0, CELL_CORDS[y][x].1-1);
        print!("{color}       {reset}");

        self.move_to(CELL_CORDS[y][x].0, CELL_CORDS[y][x].1);
        let to_print: String = format!("{color}{}{num}{}{reset}", pad.0, pad.1);
        print!("{to_print}");

        self.move_to(CELL_CORDS[y][x].0, CELL_CORDS[y][x].1+1);
        print!("{color}       {reset}");
    }

    pub fn render(&self, board: &Board) {
        for (y, row) in board.data.iter().enumerate() {
            for (x, num) in row.iter().enumerate() {
                self.write_cell(x, y, num);
            }
        }
        //Move the cursor back to the bottom
        //Note this also forces the buffer to be flushed each frame
        print!("\r\n\n");
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_write_cell() {
        let renderer = Renderer::new();
        renderer.write_cell(0, 0, &0);
        renderer.write_cell(0, 0, &2);
        renderer.write_cell(0, 0, &16);
        renderer.write_cell(0, 0, &128);
        renderer.write_cell(0, 0, &1024);
        renderer.write_cell(0, 0, &16384);
    }
}
