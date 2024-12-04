use anyhow::Result;

const DR: [[(i64, i64); 2]; 2] = [[(-1, -1), (1, 1)], [(1, 1), (-1, -1)]];
const DL: [[(i64, i64); 2]; 2] = [[(-1, 1), (1, -1)], [(1, -1), (-1, 1)]];

pub fn part_b(input: &str) -> Result<i64> {
    let input_bytes = input.as_bytes();
    let nc = input.find('\n').unwrap();
    let nr = input.len() / nc;
    let rl = nr + 1;

    let w = b"MS";

    let mut s = 0;
    for r in 1..nr - 1 {
        for c in 1..nc - 1 {
            if input_bytes[r + (c * rl)] != b'A' {
                continue;
            }
            let mut found = false;
            {
                for d in DR {
                    for (i, (dr, dc)) in d.iter().enumerate() {
                        // allow overflow
                        let (cr, cc): (usize, usize) =
                            ((r as i64 + dr) as usize, (c as i64 + dc) as usize);
                        // check for overflow
                        if input_bytes[cr + (cc * rl)] != w[i] {
                            break;
                        }
                        if i == 1 {
                            found = true;
                            break;
                        }
                    }
                    if found {
                        break;
                    }
                }
            };
            if !found {
                continue;
            }
            let mut found = false;
            {
                for d in DL {
                    for (i, (dr, dc)) in d.iter().enumerate() {
                        // allow overflow
                        let (cr, cc): (usize, usize) =
                            ((r as i64 + dr) as usize, (c as i64 + dc) as usize);
                        // check for overflow
                        if input_bytes[cr + (cc * rl)] != w[i] {
                            break;
                        }
                        if i == 1 {
                            found = true;
                            break;
                        }
                    }
                    if found {
                        break;
                    }
                }
            };
            if !found {
                continue;
            }
            s += 1;
        }
    }

    Ok(s)
}

#[cfg(test)]
mod tests {

    #[test]
    fn test_part_4_b() {
        let input = "MMMSXXMASM\nMSAMXMSMSA\nAMXSXMAAMM\nMSAMASMSMX\nXMASAMXAMM\nXXAMMXXAMA\nSMSMSASXSS\nSAXAMASAAA\nMAMMMXMMMM\nMXMXAXMASX";
        assert_eq!(super::part_b(input).unwrap(), 9);
    }
}
