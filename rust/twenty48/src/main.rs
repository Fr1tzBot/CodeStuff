use std::env;
use rand::SeedableRng;
use rand::RngExt;
use rand::rngs::StdRng;
use crate::input::get_key;
use crate::board::Board;

mod board;
mod input;

fn main() -> std::io::Result<()> {
    let args: Vec<String> = env::args().collect();
    let mut rng = match args.len() {
        2_usize => StdRng::seed_from_u64(args.get(1).unwrap().parse().unwrap()),
        _ => StdRng::from_rng(&mut rand::rng()),
    };
    let mut board = Board{data: [[0; 4]; 4], score: 0};
    board.place_first(&mut rng);
    board.print();
    while board.is_solveable() {
        let key = match get_key() {
            Some(i) => i,
            None => return Ok(()),
        };
        board.shift(&mut rng, key);
        board.print();
    }
    Ok(())
}
