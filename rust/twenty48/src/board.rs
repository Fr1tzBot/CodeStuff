use rand::RngExt;
use rand::rngs::StdRng;

#[derive(Debug, Copy, Clone)]
pub struct Board {
    pub data: [[u16; 4]; 4],
    pub score: u32
}

pub enum Dir {
    Up,
    Down,
    Left,
    Right
}

impl Board {
    fn insert_tile(&mut self, rng: &mut StdRng) {
        let mut zeros: [(usize, usize); 16] = [(4, 4); 16];
        let mut k: usize = 0;
        for (i, a) in self.data.iter().enumerate() {
            for (j, v) in a.iter().enumerate() {
                if *v == 0 { zeros[k] = (i, j); k+=1; }
            }
        }
        if k == 0 {return;}

        let val = rng.random_range(0..10) == 9;
        let pos = zeros[rng.random_range(0..k)];
        self.data[pos.0][pos.1] = if val {4} else {2};
    }

    pub fn place_first(&mut self, rng: &mut StdRng) {
        self.insert_tile(rng);
        self.insert_tile(rng);
    }

    pub fn print(&self) {
        for i in 0..4 {
            print!("{:?}", self.data[i]);
            if i == 0 { print!(" Score: {}", self.score); }
            println!();
        }
        println!();
    }

    fn reverse(&self, a: [u16; 4]) -> [u16; 4] {
        [a[3], a[2], a[1], a[0]]
    }

    fn get_col(&self, x: usize) -> [u16; 4] {
        [self.data[0][x], self.data[1][x], self.data[2][x], self.data[3][x]]
    }

    fn set_col(&mut self, x: usize, a: [u16; 4]) {
        self.data[0][x] = a[0];
        self.data[1][x] = a[1];
        self.data[2][x] = a[2];
        self.data[3][x] = a[3];
    }

    fn get_row(&self, y: usize) -> [u16; 4] { self.data[y] }

    fn set_row(&mut self, y: usize, a: [u16; 4]) { self.data[y] = a; }

    fn shift_line(&self, arr: [u16; 4], rightwards: bool) -> ([u16; 4], u32)  {
        let mut a: [u16; 4] = if rightwards {self.reverse(arr)}
        else {[0, 0, 0, 0]};
        //First, force all zeroes to the right
        let mut selected: usize = 0;
        for i in &arr {
            if *i != 0 {
                a[selected] = *i;
                selected += 1;
            }
        }

        let mut selected: usize = 0;
        let mut max: usize = 3;
        let mut scoreinc = 0;
        //This is too much code for 4 items...
        while selected < max && a[selected] != 0 {
            if a[selected] == a[selected + 1] {
                a[selected] *= 2;
                scoreinc += a[selected] as u32;
                for i in (selected+1)..max {
                    a[i] = a[i+1];
                }
                a[max] = 0;
                max -= 1;
            }
            selected += 1;
        }

        if rightwards {(self.reverse(a), scoreinc)}
        else {(a, scoreinc)}
    }

    pub fn is_solveable(&self, ) -> bool {
        //First check for zeroes (zeroes mean there must be a legal move
        for i in 0..4 {
            for j in 0..4 {
                if self.data[j][i] == 0 {return true;}
            }
        }

        //We only need to check up or down and left or right
        //Then check for Up Merges
        for i in 0..4 {
            let a = self.get_col(i);
            if self.shift_line(a, false).1 > 0 { return true; }
        }

        //Finally check for Left merges
        for i in 0..4 {
            let a = self.get_row(i);
            if self.shift_line(a, false).1 > 0 { return true; }
        }
        false
    }

    pub fn shift(&mut self, rng: &mut StdRng, dir: Dir) {
        for i in 0..4 {
            let result = match dir {
                Dir::Up =>    self.shift_line(self.get_col(i), false),
                Dir::Down =>  self.shift_line(self.get_col(i), true),
                Dir::Left =>  self.shift_line(self.get_row(i), false),
                Dir::Right => self.shift_line(self.get_row(i), true),
            };
            self.score += result.1;
            match dir {
                Dir::Up|Dir::Down => self.set_col(i, result.0),
                Dir::Left|Dir::Right => self.set_row(i, result.0),
            }
        }
        self.insert_tile(rng);
    }
}
