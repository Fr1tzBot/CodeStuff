use std::io;

fn main() {
    println!("How Deep is the lake (in meters)?");
    let mut depth = String::new();

    io::stdin().read_line(&mut depth)
        .expect("Failed to read line");

    let depth: i32 = depth.trim().parse().expect("Please type a number!");

    if depth < 12 {
        println!("You can probably dive in this if you are a beginner!");
    }

    if depth >= 12 && depth <= 30 {
        println!("You can probably dive in this if you are a trained professional!");
    }

    if depth > 30 {
        println!("You might want to make preparations before diving!");
    }

    println!("The pressure of the water is: {}", 1000.0*9.81*depth as f32);
}

