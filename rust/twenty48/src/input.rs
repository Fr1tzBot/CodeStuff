use crossterm::event::{read, Event, KeyCode};
use crossterm::terminal::{enable_raw_mode, disable_raw_mode};
use crate::board::Dir;

pub fn get_key() -> Option<Dir> {
    enable_raw_mode();
    let key: Option<Dir>;
    loop {
        match read() {
            Ok(Event::Key(event)) => {
                key = match event.code {
                    KeyCode::Up =>    Some(Dir::Up),
                    KeyCode::Down =>  Some(Dir::Down),
                    KeyCode::Left =>  Some(Dir::Left),
                    KeyCode::Right => Some(Dir::Right),
                    KeyCode::Char('q') => None,
                    _ => {continue;}
                };
                break
            },
            _ => {continue;}
        }
    }
    disable_raw_mode();
    key
}

