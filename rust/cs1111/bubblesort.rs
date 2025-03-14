use std::io;

fn bubbleSort(array: &[i32], size: i32) {
    for i in 0..size {
        if i == size - 1 {
            print!("{} ", array[i]);
        } else {
            print!("{}, ", array[i]);
        }
    }
    print!("(start)\n");

    let temp;
    let (swapcount, count) = (1, 0);

    while swapcount > 0 {
        swapcount = 0;
    }

}
