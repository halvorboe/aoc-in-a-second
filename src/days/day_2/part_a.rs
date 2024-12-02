use anyhow::Result;

pub fn part_a(input: &str) -> Result<i64> {
    let parsed: Vec<Vec<i64>> = input
        .lines()
        .map(|l| {
            l.split_whitespace()
                .map(|n| n.parse::<i64>().unwrap())
                .collect()
        })
        .collect();
    Ok(parsed
        .into_iter()
        .map(|row| {
            let (negative, positive): (Vec<bool>, Vec<bool>) = row
                .windows(2)
                .map(|p| p[1] - p[0])
                .map(|d| (d > 0 && d < 4, d > -4 && d < 0))
                .unzip();
            match negative.into_iter().all(|b| b) || positive.into_iter().all(|b| b) {
                true => 1,
                false => 0,
            }
        })
        .sum())
}

#[cfg(test)]
mod tests {

    #[test]
    fn test_part_a() {
        let input = "7 6 4 2 1\n1 2 7 8 9\n9 7 6 2 1\n1 3 2 4 5\n8 6 4 4 1\n1 3 6 7 9";
        assert_eq!(super::part_a(input).unwrap(), 2);
    }
}
