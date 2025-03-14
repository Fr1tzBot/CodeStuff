use std::io;

fn bubbleSort(array: &mut[i32], size: i32) {
    let mut size: usize = size as usize;

    for i in 0..size {
        if i == size - 1 {
            print!("{} ", array[i]);
        } else {
            print!("{}, ", array[i]);
        }
    }
    println!("(start)");

    let mut temp: i32;
    let (mut swapcount, mut count) = (1, 0);

    while swapcount > 0 {
        swapcount = 0;
        for i in 1..size {
            if count > 0 {print!("\n");}
            if array[i-1] > array[i] {
                temp = array[(i)];
                array[i] = array[i-1];
                array[i-1] = temp;
                swapcount += 1;
            }

            for j in 0..size {
                if j == size - 1 {
                    print!("{} ", array[j]);
                } else {
                    print!("{}, ", array[j]);
                }
            }

            print!("({}, {})", i-1, i);

            count += 1;
        }
    }

    println!(" (done)");
}

fn main() {
    let mut data = [7, 4, 2];
    bubbleSort(&mut data, 3);
}

