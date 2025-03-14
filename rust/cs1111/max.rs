use std::io;

fn max(a: i32, b: i32, c: i32) -> i32 {
    let mut max = a;

    if b > max {
        max = b;
    }

    if c > max {
        max = c;
    }

    return max;
}

fn main() {
    let (mut a, mut b, mut c) = (String::new(), String::new(), String::new());

    io::stdin().read_line(&mut a).expect("failed to read a.");
    io::stdin().read_line(&mut b).expect("failed to read b.");
    io::stdin().read_line(&mut c).expect("failed to read c.");

    let a: i32 = a.trim().parse().expect("failed to parse.");
    let b: i32 = b.trim().parse().expect("failed to parse.");
    let c: i32 = c.trim().parse().expect("failed to parse.");

    println!("The maximum value is {}", max(a, b, c));
}

