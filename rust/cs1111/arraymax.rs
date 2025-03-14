use std::io;

fn maxValue(array: &[i32], size: i32) -> i32 {
    let mut max = array[0];
    for i in 1..size {
        match array.get(i as usize) {
            Some(arval) => {
                if *arval > max {
                    max = *arval;
                    println!("max is {}", max);
                }
            },
            None => println!("out of bounds or somethin"),
        }
    }
    return max;
}

fn main() {
    let a: [i32; 6] = [1, 4, 5, 10, 8, 9];
    let b: [i32; 8] = [4, 5, 60, 5, 1, 100, 8, 10];

    println!("max in array a is {}", maxValue(&a, 6));
    println!("max in array b is {}", maxValue(&b, 8));
}

