use anyhow::Result;

const D: [(i64, i64); 8] = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
];

pub fn part_a(input: &str) -> Result<i64> {
    let input_bytes = input.as_bytes();
    let nc = input.find('\n').unwrap();
    let nr = input.len() / nc;
    let rl = nr + 1;

    let w = b"XMAS";

    let mut s = 0;
    for r in 0..nr {
        for c in 0..nc {
            if input_bytes[r + (c * rl)] != w[0] {
                continue;
            }
            for (dr, dc) in D.iter() {
                for i in 1..w.len() {
                    // allow overflow
                    let (cr, cc): (usize, usize) = (
                        (r as i64 + dr * i as i64) as usize,
                        (c as i64 + dc * i as i64) as usize,
                    );
                    // check for overflow
                    if cr >= nr || cc >= nc {
                        break;
                    }
                    if input_bytes[cr + (cc * rl)] != w[i] {
                        break;
                    }
                    // if we are at the end of the word
                    if i == w.len() - 1 {
                        s += 1;
                    }
                }
            }
        }
    }

    Ok(s)
}

#[cfg(test)]
mod tests {

    #[test]
    fn test_part_4_a() {
        let input = "MMMSXXMASM\nMSAMXMSMSA\nAMXSXMAAMM\nMSAMASMSMX\nXMASAMXAMM\nXXAMMXXAMA\nSMSMSASXSS\nSAXAMASAAA\nMAMMMXMMMM\nMXMXAXMASX";
        assert_eq!(super::part_a(input).unwrap(), 18);
    }
}
