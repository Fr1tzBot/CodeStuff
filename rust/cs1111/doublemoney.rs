use std::io;

fn main() {
    println!("What is the yearly return rate in percentage?");
    let mut rate = String::new();

    io::stdin().read_line(&mut rate).expect("Failed to read percentage");

    let mut rate: f32 = rate.trim().parse().expect("Parsing failed.");

    rate /= 100.0;
    rate += 1.0;

    let mut years = 0;
    let mut total = 1.0;

    while total < 2.0 {
        total *= rate;
        years += 1;
    }

    println!("With the return rate of {}, it will take {} years to double my money.", (rate-1.0)*100.0, years);
}

