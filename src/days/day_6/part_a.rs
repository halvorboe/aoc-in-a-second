use anyhow::Result;

use crate::days::day_6::parse_input;

use super::Direction;

pub fn part_a(input: &str) -> Result<i64> {
    let (n_r, n_c, mut guard, walls) = parse_input(input);
    let mut visited = vec![false; n_r * n_c];

    loop {
        let (r, c, d) = guard;
        visited[r * n_r + c] = true;
        let (next_r, next_c) = match d {
            Direction::Up => (r - 1, c),
            Direction::Down => (r + 1, c),
            Direction::Left => (r, c - 1),
            Direction::Right => (r, c + 1),
        };
        // out of bounds
        if next_r >= n_r || next_c >= n_c {
            break;
        }
        if walls[next_r * n_r + next_c] {
            guard = (r, c, d.turn_right());
        } else {
            guard = (next_r, next_c, d);
        }
    }
    Ok(visited
        .iter()
        .map(|b| match b {
            true => 1,
            false => 0,
        })
        .sum())
}

#[cfg(test)]
mod tests {

    #[test]
    fn test_part_6_a() {
        let input = "....#.....\n.........#\n..........\n..#.......\n.......#..\n..........\n.#..^.....\n........#.\n#.........\n......#...";
        assert_eq!(super::part_a(input).unwrap(), 41);
    }
}
