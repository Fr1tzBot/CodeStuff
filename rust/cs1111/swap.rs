use std::io;

fn swap(a: &mut i32, b: &mut i32) {
    let temp = *a;
    *a = *b;
    *b = temp;
}

fn main() {
    let (mut a, mut b) = (0, 1);

    swap(&mut a, &mut b);

    println!("{}, {}", a, b);
}

