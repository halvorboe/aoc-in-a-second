use anyhow::Result;

pub fn part_a(input: &str) -> Result<i64> {
    let input_bytes = input.as_bytes();
    let mut sum = 0;
    let mut pointer = 0;
    while pointer < input.len() - 4 {
        // if we find a mul
        if &input_bytes[pointer..pointer + 4] == b"mul(" {
            pointer += 4;
        } else {
            pointer += 1;
            continue;
        }
        // parse first number
        let mut first = 0;
        while input_bytes[pointer] >= '0' as u8 && input_bytes[pointer] <= '9' as u8 {
            first = first * 10 + (input_bytes[pointer] - '0' as u8) as i64;
            pointer += 1;
        }
        if first == 0 {
            continue;
        }
        if input_bytes[pointer] != ',' as u8 {
            continue;
        }
        pointer += 1;
        // parse second number
        let mut second = 0;
        while input_bytes[pointer] >= '0' as u8 && input_bytes[pointer] <= '9' as u8 {
            second = second * 10 + (input_bytes[pointer] - '0' as u8) as i64;
            pointer += 1;
        }
        if second == 0 {
            continue;
        }
        if input_bytes[pointer] != ')' as u8 {
            pointer += 1;
            continue;
        }
        sum += first * second;
    }
    Ok(sum)
}

#[cfg(test)]
mod tests {

    #[test]
    fn test_part_3_a() {
        let input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))";
        assert_eq!(super::part_a(input).unwrap(), 161);
    }
}
