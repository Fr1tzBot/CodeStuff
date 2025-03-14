use std::io;

fn myabs(x: f32) -> f32 {
    if x < 0.0 {
        return -x;
    }
    else {
        return x;
    }
}

fn main() {
    let mut data = -3.4;
    println!("abs({})={}", data, myabs(data));
    data=3.4;
    println!("abs({})={}", data, myabs(data));
}

