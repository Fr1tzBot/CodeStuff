use std::io;

fn numsuffix(num: i32) -> String {
    return match num as u32 {
        1 => "st",
        2 => "nd",
        3 => "rd",
        _ => "th",
    }.to_string();
}

fn search(array: &[i32], value: i32, size: usize) -> usize {
    let mut low: usize = 0;
    let mut high: usize = size-1;
    let mut mid: usize;

    while low <= high {
        mid = (low+high)/2;

        if value < array[low] { return low; }

        if value > array[high] { return high + 1; }

        if value > array[mid] {
            low = mid + 1;
        } else if value < array[mid] {
            high = mid - 1;
        }
    }
    return 99999;
}

fn insertionSort(array: &mut[i32], size: usize) {
    for i in 0..size {
        if i < size - 1 {
            print!("{}, ", array[i]);
        } else {
            print!("{} ", array[i]);
        }
    }

    let (mut key, mut index);

    print!("(start)");

    for i in 1..size {
        print!("\n");
        key = array[i];
        index = search(&array, key, i);

        for k in (index+1)..(i+1) {
            print!("\nreplaced {} with {}\n", array[k], array[k-1]);
            array[k] = array[k-1];
        }

        for h in 0..size {
            print!("{}", array[h]);
        }
        print!("\n");

        array[index] = key;

        for j in 0..size {
            if j < size - 1 {
                print!("{}, ", array[j]);
            } else {
                print!("{} ", array[j]);
            }
        }
        print!("({}{} step)", i, numsuffix(i as i32));
    }

    println!(" (done)");
}

fn main() {
    let mut array = [7, 4, 2, 9];
    insertionSort(&mut array, 4);
}

