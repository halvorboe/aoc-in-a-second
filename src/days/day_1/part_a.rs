use std::iter::zip;

use anyhow::Result;

pub fn part_a(input: &str) -> Result<i64> {
    let (mut first, mut second): (Vec<i64>, Vec<i64>) = input
        .lines()
        .map(|line| line.split_once("   ").unwrap())
        .map(|(a, b)| (a.parse::<i64>().unwrap(), b.parse::<i64>().unwrap()))
        .unzip();

    first.sort_unstable();
    second.sort_unstable();

    Ok(zip(first.into_iter(), second.into_iter())
        .map(|(a, b)| (a - b).abs())
        .sum::<i64>())
}

#[cfg(test)]
mod tests {

    #[test]
    fn test_part_a() {
        let input = "3   4\n4   3\n2   5\n1   3\n3   9\n3   3";
        assert_eq!(super::part_a(input).unwrap(), 11);
    }
}
