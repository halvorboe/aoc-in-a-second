use anyhow::Result;

pub fn part_a(_input: &str) -> Result<i64> {
    Ok(0)
}

#[cfg(test)]
mod tests {

    #[test]
    fn test_part_7_a() {
        let input = "";
        assert_eq!(super::part_a(input).unwrap(), 0);
    }
}
