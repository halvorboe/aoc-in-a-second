pub mod part_a;
pub mod part_b;

pub use part_a::part_a;
pub use part_b::part_b;

#[derive(Debug, Clone, Copy)]
enum Direction {
    Up,
    Down,
    Left,
    Right,
}

impl Direction {
    fn turn_right(&self) -> Self {
        match self {
            Direction::Up => Direction::Right,
            Direction::Right => Direction::Down,
            Direction::Down => Direction::Left,
            Direction::Left => Direction::Up,
        }
    }

    fn index(&self) -> usize {
        match self {
            Direction::Up => 0,
            Direction::Right => 1,
            Direction::Down => 2,
            Direction::Left => 3,
        }
    }
}

type Guard = (usize, usize, Direction);

fn parse_input(input: &str) -> (usize, usize, Guard, Vec<bool>) {
    let mut guard = (0, 0, Direction::Down);
    let mut walls: Vec<bool> = Vec::with_capacity(input.len());
    let mut row = 0;
    let mut column = 0;
    let mut num_columns = 0;
    for c in input.chars() {
        match c {
            '\n' => {
                row += 1;
                if num_columns == 0 {
                    num_columns = column;
                } else {
                    if num_columns != column {
                        panic!("Number of columns is not consistent");
                    }
                }
                column = 0;
            }
            '.' => {
                walls.push(false);
                column += 1;
            }
            '#' => {
                walls.push(true);
                column += 1
            }
            '^' => {
                guard = (row, column, Direction::Up);
                walls.push(false);
                column += 1;
            }
            '<' => {
                guard = (row, column, Direction::Left);
                walls.push(false);
                column += 1;
            }
            '>' => {
                guard = (row, column, Direction::Right);
                walls.push(false);
                column += 1;
            }
            'v' => {
                guard = (row, column, Direction::Down);
                walls.push(false);
                column += 1;
            }
            _ => {
                panic!("Unknown character: {}", c);
            }
        }
    }
    let n_r = row + 1;
    let n_c = num_columns;
    (n_r, n_c, guard, walls)
}
