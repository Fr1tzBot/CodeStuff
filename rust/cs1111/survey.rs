use std::io;

fn main() {
    let myArray = [1, 3, 5, 4, 7, 2, 99, 16, 45, 67, 89, 45];

    let mut total = 0;

    for i in myArray {
        total += i;
    }

    println!("{}", total);
}

