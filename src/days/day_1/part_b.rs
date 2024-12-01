use std::collections::HashMap;

use anyhow::Result;

pub fn part_b(input: &str) -> Result<i64> {
    let mut second = HashMap::with_capacity(1000);
    let first: Vec<i64> = input
        .lines()
        .map(|line| {
            let mut it = line.split_whitespace().map(|n| n.parse::<i64>().unwrap());
            (it.next().unwrap(), it.next().unwrap())
        })
        .map(|(a, b)| {
            if let Some(entry) = second.get_mut(&b) {
                *entry += 1;
            } else {
                second.insert(b, 1);
            }
            a
        })
        .collect();

    Ok(first
        .into_iter()
        .map(|a| {
            let b = second.get(&a).unwrap_or(&0i64);
            a * b
        })
        .sum::<i64>())
}

#[cfg(test)]
mod tests {

    #[test]
    fn test_part_b() {
        let input = "3   4\n4   3\n2   5\n1   3\n3   9\n3   3";
        assert_eq!(super::part_b(input).unwrap(), 31);
    }
}
