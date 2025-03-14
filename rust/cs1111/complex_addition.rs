use std::io;

fn complexMult(a: i32, b: i32) -> i32 {
    let mut result: i32 = 0;
    for i in 0..b {
        result += a;
    }
    return result;
}

fn complexDiv(a: i32, b: i32) -> i32 {
    let mut result: i32 = a;
    let mut count: i32 = 0;

    while result >= b {
        result -= b;
        count += 1;
    }

    return count;
}

fn main() {
    let mut x = String::new();
    let mut y = String::new();


    println!("Enter Two Numbers:");
    io::stdin().read_line(&mut x).expect("Please enter a number!");
    io::stdin().read_line(&mut y).expect("Please enter a number!");

    let x: i32 = x.trim().parse().expect("Please fuck off!");
    let y: i32 = y.trim().parse().expect("No Seriously!");

    println!("30 * 4: {}\n30 / 4: {}", complexMult(x, y), complexDiv(x, y));
}


