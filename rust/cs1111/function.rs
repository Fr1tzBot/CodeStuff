use std::io;

fn printStars(stars: i32) {
    for _i in 0..stars {
        print!("*");
    }
    print!("\n");
}

fn main() {
    let mut stars = String::new();

    println!("Please enter a position integer:");
    io::stdin().read_line(&mut stars).expect("Failed to read.");

    let stars: i32 = stars.trim().parse().expect("Failed to parse.");

    for i in 1..(stars+1) {
        printStars(i);
    }
}

