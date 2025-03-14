use std::io;

fn main() {
    let mut numBooks = String::new();

    println!("How many textbooks did you buy this semester?");
    io::stdin().read_line(&mut numBooks)
        .expect("Failed to read line");

    let numBooks: i32 = numBooks.trim().parse()
        .expect("Please type a number!");

    if numBooks < 0 {
        println!("You can't buy a negative number of textbooks!");
        return;
    }

    match numBooks {
        0 => println!("You got away easy this semester!"),
        1|2|3 => println!("That's a normal amount to pay for."),
        _ => println!("You bought {} textbooks this semester.", numBooks),
    }
}

