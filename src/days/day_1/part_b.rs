use std::collections::HashMap;

use anyhow::Result;

pub fn part_b(input: &str) -> Result<i64> {
    let mut first = Vec::new();
    // OPTIMIZE: with_capacity to pre-allocate 1000 capacity for a 20% speedup.
    let mut second = HashMap::new();
    input
        .lines()
        .map(|line| line.split_once("   ").unwrap())
        .map(|(a, b)| (a.parse::<i64>().unwrap(), b.parse::<i64>().unwrap()))
        .for_each(|(a, b)| {
            first.push(a);
            second.entry(b).and_modify(|c| *c += 1).or_insert(1);
        });

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
