
fn getFib(fibnum: u32) -> u64 {
    if fibnum == 0 { return 0; }
    if fibnum == 1 || fibnum == 2 { return 1; }

    let mut cache: [u64; 10] = [0,0,0,0,0,0,0,0,0,0];

    cache[0] = 0;
    cache[1] = 1;
    cache[2] = 1;

    return fibCache(fibnum, &mut cache);
}

fn fibCache(fibnum: u32, cache: &mut [u64]) -> u64 {
    for i in 0..=fibnum as usize {
        if i == 0 || i == 1 || i == 2 { continue; }

        cache[i] = cache[i-1] + cache[i-2];
    }

    return cache[fibnum as usize];
}

fn main() {
    for i in 0..10 {
        println!("Fibonacci #{} is {}", i, getFib(i));
    }
}

