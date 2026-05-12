use std::io::{stdin,Read};
use crate::board::Dir;


pub fn get_key() -> Option<Dir> {
    for byte in stdin().bytes() {
        match byte.unwrap() {
            b'q' => return None,
            b'w' => return Some(Dir::Up),
            b'a' => return Some(Dir::Left),
            b's' => return Some(Dir::Down),
            b'd' => return Some(Dir::Right),
            _ => continue
        };
    }
    None
}

