use anyhow::Result;

pub fn part_b(_input: &str) -> Result<i64> {
    Ok(0)
}

#[cfg(test)]
mod tests {

    #[test]
    fn test_part_b() {
        let input = "";
        assert_eq!(super::part_b(input).unwrap(), 0);
    }
}
