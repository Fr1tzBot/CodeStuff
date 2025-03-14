use std::io;

fn main() {
    let mut op = String::new();

    println!("Please enter an op:");

    io::stdin().read_line(&mut op).expect("Failed to read.");

    let op: char = op.chars().nth(0).expect("Op not found.");

    match op {
        '+' => println!("Addition"),
        '-' => println!("Subtraction"),
        '*' => println!("Multiplication"),
        '/' => println!("Division"),
        '%' => println!("Modulo"),
        '>' => println!("Greater Than"),
        '<' => println!("Less Than"),
        '!' => println!("Not"),
        _   => println!("Unknown"),
    }
}

