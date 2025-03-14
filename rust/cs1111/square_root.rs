use std::io;

fn sqrtEst(x: f32, N: f32) -> f32 {
    return (x+N/x)/2.0;
}

fn main() {
    println!("Give N and i");
    let mut N = String::new();
    let mut i = String::new();

    io::stdin().read_line(&mut N).expect("Failed to read N");
    io::stdin().read_line(&mut i).expect("Failed to read i");

    let N: f32 = N.trim().parse().expect("Failed to parse N.");
    let i: i32 = i.trim().parse().expect("Failed to parse i.");

    //initial guess
    let mut x = 10.0;

    for _j in 0..i {
        x = sqrtEst(x, N);
    }

    println!("Estimate: {}", x);
}

