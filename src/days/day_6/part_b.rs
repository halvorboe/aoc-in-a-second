use anyhow::Result;

use super::{parse_input, Direction, Guard};

pub fn part_b(input: &str) -> Result<i64> {
    let (n_r, n_c, mut guard, walls) = parse_input(input);
    let mut visited = vec![[false; 4]; n_r * n_c];
    let mut loops = 0;

    loop {
        let (r, c, d) = guard;
        visited[r * n_r + c][d.index()] = true;
        let (next_r, next_c) = match d {
            Direction::Up => (r.overflowing_sub(1).0, c),
            Direction::Down => (r + 1, c),
            Direction::Left => (r, c.overflowing_sub(1).0),
            Direction::Right => (r, c + 1),
        };
        if next_r >= n_r || next_c >= n_c {
            break;
        }
        if walls[next_r * n_r + next_c] {
            guard = (r, c, d.turn_right());
        } else {
            if is_loop(&walls, &visited, &guard, n_r, n_c) {
                loops += 1;
            }
            guard = (next_r, next_c, d);
        }
    }

    Ok(loops)
}

#[inline]
fn is_loop(
    walls: &Vec<bool>,
    start_visited: &Vec<[bool; 4]>,
    start_guard: &Guard,
    n_r: usize,
    n_c: usize,
) -> bool {
    let (r, c, d) = start_guard;
    let mut guard = (*r, *c, d.turn_right());
    let mut visited = start_visited.clone();
    loop {
        let (r, c, d) = guard;
        if visited[r * n_r + c][d.index()] {
            return true;
        }
        visited[r * n_r + c][d.index()] = true;
        let (next_r, next_c) = match d {
            Direction::Up => (r.overflowing_sub(1).0, c),
            Direction::Down => (r + 1, c),
            Direction::Left => (r, c.overflowing_sub(1).0),
            Direction::Right => (r, c + 1),
        };
        if next_r >= n_r || next_c >= n_c {
            break;
        }
        if walls[next_r * n_r + next_c] {
            guard = (r, c, d.turn_right());
        } else {
            guard = (next_r, next_c, d);
        }
    }
    false
}

#[cfg(test)]
mod tests {

    #[test]
    fn test_part_6_b() {
        let input = "....#.....\n.........#\n..........\n..#.......\n.......#..\n..........\n.#..^.....\n........#.\n#.........\n......#...";
        assert_eq!(super::part_b(input).unwrap(), 6);
    }
}
