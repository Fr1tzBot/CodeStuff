use std::env;
use std::time::{SystemTime, UNIX_EPOCH};
use crate::input::get_key;
use crate::render::Renderer;
use crate::board::Board;
mod board;
mod input;
mod render;


fn main() -> std::io::Result<()> {
    let args: Vec<String> = env::args().collect();

    //Use unix time as seed if no seed is provided
    let seed: u64 = match args.len() {
        2_usize => args.get(1).unwrap().parse().unwrap(),
        _ => SystemTime::now().duration_since(UNIX_EPOCH).unwrap().as_secs()
    };

    //Set up and display initial board
    let mut board = Board::new(seed);
    let renderer = Renderer::new();
    board.place_first();
    renderer.render(&board);

    while board.is_solveable() {
        let key = match get_key() {
            Some(i) => i,
            None => return Ok(()),
        };
        board.shift(key);
        renderer.render(&board);
    }
    Ok(())
}
