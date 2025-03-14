use std::io;

fn main() {
    println!("Enter 3 numbers (a, b, n)");
    let mut a = String::new();
    let mut b = String::new();
    let mut n = String::new();

    let mut msg = "Failed to read var".to_string();

    io::stdin().read_line(&mut a).expect(&msg);
    io::stdin().read_line(&mut b).expect(&msg);
    io::stdin().read_line(&mut n).expect(&msg);

    msg = "Failed to convert to int.".to_string();

    let mut a: i32 = a.trim().parse().expect(&msg);
    let mut b: i32 = b.trim().parse().expect(&msg);
    let n: i32 = n.trim().parse().expect(&msg);

    let mut next;

    for i in 0..n {
        println!("{}", a);
        next = a + b;

        a = b;
        b = next;
    }
}

