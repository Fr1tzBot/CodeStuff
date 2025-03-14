use std::io;

fn main() {
    let mut a = String::new();
    let mut b = String::new();

    println!("Enter Two Numbers: ");
    io::stdin().read_line(&mut a).expect("Failed to read line");
    io::stdin().read_line(&mut b).expect("Failed to read line");

    println!("Are the numbers equal?");

    if a == b {
        println!("Yes");
    } else {
        println!("No");
    }

    println!("Are the numbers not equal?");

    if a != b {
        println!("Yes");
    } else {
        println!("No");
    }

    println!("Is the first number less than the second number?");

    if a < b {
        println!("Yes");
    } else {
        println!("No");
    }

    println!("Is the first number greater than the second number?");

    if a > b {
        println!("Yes");
    } else {
        println!("No");
    }

    println!("Is the first number less than or equal to the second number?");

    if a <= b {
        println!("Yes");
    } else {
        println!("No");
    }

    println!("Is the first number greater than or equal to the second number?");

    if a >= b {
        println!("Yes");
    } else {
        println!("No");
    }
}

