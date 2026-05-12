use rand::SeedableRng;
use rand::RngExt;
use rand::rngs::StdRng;

#[derive(Debug)]
pub struct Board {
    pub data: [[u16; 4]; 4],
    pub score: u32,
    pub rng: StdRng
}

pub enum Dir {
    Up,
    Down,
    Left,
    Right
}

impl Board {
    pub fn new(seed: u64) -> Self {
        Self {data: [[0; 4]; 4],
              score: 0,
              rng: StdRng::seed_from_u64(seed)}
    }

    pub fn get_flattened_data(&self) -> [u16; 16] {
        [self.data[0][0], self.data[0][1], self.data[0][2], self.data[0][3],
         self.data[1][0], self.data[1][1], self.data[1][2], self.data[1][3],
         self.data[2][0], self.data[2][1], self.data[2][2], self.data[2][3],
         self.data[3][0], self.data[3][1], self.data[3][2], self.data[3][3]]
    }

    fn count_full_tiles(&self) -> i8 {
        let mut output: i8 = 0;
        for i in 0..4 {
            for j in 0..4 {
                if self.data[i][j] != 0 { output += 1; }
            }
        }
        output
    }

    /// Adds a new tile after the player's move
    /// Places a 4 (10% chance) or a 2 (90% chance) at a random position in the grid
    fn insert_tile(&mut self) {
        let mut zeros: [(usize, usize); 16] = [(4, 4); 16];
        let mut k: usize = 0;
        for (i, a) in self.data.iter().enumerate() {
            for (j, v) in a.iter().enumerate() {
                if *v == 0 { zeros[k] = (i, j); k+=1; }
            }
        }
        if k == 0 {return;}

        let val = self.rng.random_range(0..10) == 9;
        let pos = zeros[self.rng.random_range(0..k)];
        self.data[pos.0][pos.1] = if val {4} else {2};
    }

    /// Inserts the first two tiles of the game
    /// Runs insert_tile twice, placing a 4 (10% chance) or a 2 (90% chance) at two unique, random positions on the grid.
    pub fn place_first(&mut self) {
        self.insert_tile();
        self.insert_tile();
    }

    /// Converts the data in the grid as well as the score to a string.
    /// Prints the grid with whitespace between, prints the score after the first row
    pub fn to_string(&self) -> String {
        format!("{:?} Score: {}\n{:?}\n{:?}\n{:?}\n", self.data[0], self.score, self.data[1], self.data[2], self.data[3])
    }

    /// Returns a row in the grid reversed
    fn reverse(&self, a: [u16; 4]) -> [u16; 4] {
        [a[3], a[2], a[1], a[0]]
    }

    /// Returns a given column (x-coordinate) of the grid
    pub fn get_col(&self, x: usize) -> [u16; 4] {
        [self.data[0][x], self.data[1][x], self.data[2][x], self.data[3][x]]
    }

    /// Sets a given column (x-coordinate) to the provided values
    fn set_col(&mut self, x: usize, a: [u16; 4]) {
        self.data[0][x] = a[0];
        self.data[1][x] = a[1];
        self.data[2][x] = a[2];
        self.data[3][x] = a[3];
    }

    /// Returns a given row (y-coordinate) of the grid
    pub fn get_row(&self, y: usize) -> [u16; 4] { self.data[y] }

    /// Sets a given row (y-coordinate) to the provided values
    fn set_row(&mut self, y: usize, a: [u16; 4]) { self.data[y] = a; }

    /// Shifts a row or column in the provided direction, combining neighboring values that are equal
    /// Produces no movement if row is full and has no neighboring equal values
    /// Returns a tuple containing the shifted output and the number of points scored in this shift
    fn shift_line(&self, arr: [u16; 4], rightwards: bool) -> ([u16; 4], u32)  {
        let mut output = [0, 0, 0, 0];
        let mut scoreinc: u32 = 0;

        //Simple, known zero-score cases first
        //Note its not worth checking if there are no neighboring equal values
        if arr == [0, 0, 0, 0] {
            return (output, scoreinc)
        }


        let mut a = arr;
        if rightwards {a=self.reverse(arr);}
        let mut vals: Vec<u16> = a.iter().copied().filter(|&x| x !=0).collect();
        let mut i = 0;
        while i+1 < vals.len() {
            if vals[i] == vals[i+1] {
                vals[i] *= 2;
                scoreinc += vals[i] as u32;
                vals.remove(i+1);
            }
            i += 1;
        }

        while vals.len() < 4 {
            vals.push(0);
        }

        output = *vals.as_array().unwrap();
        if rightwards {output=self.reverse(output);}

        (output, scoreinc)
    }

    /// Check if the current grid has moved remaining
    /// First checks if any slots are still zero on the board, then runs shifts in all cardinal directions, checking for scoring
    pub fn is_solveable(&self, ) -> bool {
        //First check for zeroes (zeroes mean there must be a legal move)
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

    /// Maps the shift_line function to a Dir enum
    /// Calls shift_line with rightwards=true for Dir::Down and Dir::Right, false otherwise
    /// Increments score and runs insert_tile after calling
    pub fn shift(&mut self, dir: Dir) {
        for i in 0..4 {
            let result = match dir {
                Dir::Up    => self.shift_line(self.get_col(i), false),
                Dir::Down  => self.shift_line(self.get_col(i), true),
                Dir::Left  => self.shift_line(self.get_row(i), false),
                Dir::Right => self.shift_line(self.get_row(i), true),
            };
            self.score += result.1;
            match dir {
                Dir::Up|Dir::Down    => self.set_col(i, result.0),
                Dir::Left|Dir::Right => self.set_row(i, result.0),
            }
        }
        self.insert_tile();
    }

}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_insert_tile() {
        let mut board = Board::new(0);
        for i in 1..=16 {
            board.insert_tile();
            assert_eq!(board.count_full_tiles(), i);
        }

        board.insert_tile();
        assert_eq!(board.count_full_tiles(), 16);
    }

    #[test]
    fn test_place_first() {
        let mut board = Board::new(0);
        board.place_first();
        assert_eq!(board.count_full_tiles(), 2);
    }

    #[test]
    fn test_to_string() {
        let board = Board::new(0);
        assert_eq!(board.to_string(),
        "[0, 0, 0, 0] Score: 0\n[0, 0, 0, 0]\n[0, 0, 0, 0]\n[0, 0, 0, 0]\n");
    }

    #[test]
    fn test_reverse() {
        let board = Board::new(0);
        let arr = [1, 2, 3, 4];
        assert_eq!([4, 3, 2, 1], board.reverse(arr));
    }

    #[test]
    fn test_get_row_rand() {
        let mut board = Board::new(1232435465);
        for _i in 0..16 {
            board.insert_tile();
        }
        assert_eq!([2, 4, 2, 4], board.get_row(2));
    }

    #[test]
    fn test_get_col_rand() {
        let mut board = Board::new(0);
        for _i in 0..8 {
            board.insert_tile();
        }
        assert_eq!([2, 0, 2, 0], board.get_col(3));
    }

    #[test]
    fn test_set_row() {
        let mut board = Board::new(0);
        let arr = [1, 2, 3, 4];
        for i in 0..4 {
            board.set_row(i, arr);
            assert_eq!(board.get_row(i), arr);
        }

    }

    #[test]
    fn test_set_col() {
        let mut board = Board::new(0);
        let arr = [1, 2, 3, 4];
        for i in 0..4 {
            board.set_col(i, arr);
            assert_eq!(board.get_col(i), arr);
        }

    }

    #[test]
    fn test_shift_line_noscore_left() {
        let board = Board::new(0);
        let zeroes = [0, 0, 0, 0];
        let full = [1, 2, 3, 4];
        assert_eq!(board.shift_line(zeroes, false), ([0, 0, 0, 0], 0));
        assert_eq!(board.shift_line(full, false), ([1, 2, 3, 4], 0));
    }

    #[test]
    fn test_shift_line_noscore_right() {
        let board = Board::new(0);
        let zeroes = [0, 0, 0, 0];
        let full = [1, 2, 3, 4];
        assert_eq!(board.shift_line(zeroes, true), ([0, 0, 0, 0], 0));
        assert_eq!(board.shift_line(full, true), ([1, 2, 3, 4], 0));
    }

    #[test]
    fn test_shift_line_basic() {
        let board = Board::new(0);
        let t1 =   [2, 2, 0, 0];
        let s1_l = [4, 0, 0, 0];
        let s1_r = [0, 0, 0, 4];
        assert_eq!(board.shift_line(t1, false), (s1_l, 4));
        assert_eq!(board.shift_line(t1, true), (s1_r, 4));

        let t1 =   [0, 2, 2, 0];
        let s1_l = [4, 0, 0, 0];
        let s1_r = [0, 0, 0, 4];
        assert_eq!(board.shift_line(t1, false), (s1_l, 4));
        assert_eq!(board.shift_line(t1, true), (s1_r, 4));

        let t1 =   [0, 0, 2, 2];
        let s1_l = [4, 0, 0, 0];
        let s1_r = [0, 0, 0, 4];
        assert_eq!(board.shift_line(t1, false), (s1_l, 4));
        assert_eq!(board.shift_line(t1, true), (s1_r, 4));

        let t1 =   [0, 2, 2, 0];
        let s1_l = [4, 0, 0, 0];
        let s1_r = [0, 0, 0, 4];
        assert_eq!(board.shift_line(t1, false), (s1_l, 4));
        assert_eq!(board.shift_line(t1, true), (s1_r, 4));
    }

    #[test]
    fn test_shift_line_complex() {
        let board = Board::new(0);

        let t1 =   [2, 2, 2, 2];
        let s1_l = [4, 4, 0, 0];
        let s1_r = [0, 0, 4, 4];
        assert_eq!(board.shift_line(t1, false), (s1_l, 8));
        assert_eq!(board.shift_line(t1, true), (s1_r, 8));

        let t1 =   [2, 2, 4, 4];
        let s1_l = [4, 8, 0, 0];
        let s1_r = [0, 0, 4, 8];
        assert_eq!(board.shift_line(t1, false), (s1_l, 12));
        assert_eq!(board.shift_line(t1, true), (s1_r, 12));

        let t1 =   [2, 2, 4, 8];
        let s1_l = [4, 4, 8, 0];
        let s1_r = [0, 4, 4, 8];
        assert_eq!(board.shift_line(t1, false), (s1_l, 4));
        assert_eq!(board.shift_line(t1, true), (s1_r, 4));
    }

    #[test]
    fn test_is_solveable() {
        let mut board = Board::new(0);
        assert!(board.is_solveable());
        for _i in 0..16 {
            board.insert_tile();
        }
        assert!(board.is_solveable());
        board.set_col(0, [1, 2, 3, 4]);
        board.set_col(1, [4, 3, 2, 1]);
        board.set_col(2, [1, 2, 3, 4]);
        board.set_col(3, [4, 3, 2, 1]);
        assert!(!board.is_solveable());
    }
}
