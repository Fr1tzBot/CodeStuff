use std::io;

fn main() {
    let mut num = 5;
    let mut rate = 5.4;
    let mut letter = 'B';

    let mut numP = &mut num;
    let mut rateP = &mut rate;
    let mut letterP = &mut letter;

    (*numP) += 1;
    (*rateP) += 1.0;
    (*letterP) = 'a';

    println!("numP: {}, *numP: {}", numP, *numP);
    println!("rateP: {}, *rateP: {}", rateP, *rateP);
    println!("letterP: {}, *letterP: {}", letterP, *letterP);
}

