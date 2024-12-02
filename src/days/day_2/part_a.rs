use anyhow::Result;
use itertools::Itertools;

pub fn part_a(input: &str) -> Result<i64> {
    Ok(input
        .lines()
        .map(|l| {
            let (negative, positive): (bool, bool) = l
                .split_whitespace()
                .map(|n| n.parse::<i64>().unwrap())
                .tuple_windows()
                .map(|(a, b)| b - a)
                .map(|d| (d > 0 && d < 4, d > -4 && d < 0))
                .fold((true, true), |(negative, positive), (n, p)| {
                    (negative && n, positive && p)
                });

            match negative || positive {
                true => 1,
                false => 0,
            }
        })
        .sum())
}

#[cfg(test)]
mod tests {

    #[test]
    fn test_part_2_a() {
        let input = "7 6 4 2 1\n1 2 7 8 9\n9 7 6 2 1\n1 3 2 4 5\n8 6 4 4 1\n1 3 6 7 9";
        assert_eq!(super::part_a(input).unwrap(), 2);
    }
}
