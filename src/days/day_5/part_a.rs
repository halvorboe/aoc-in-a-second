use anyhow::Result;

pub fn part_a(input: &str) -> Result<i64> {
    let (a, b) = input.split_once("\n\n").unwrap();
    let mut rules: [[bool; 100]; 100] = [[false; 100]; 100];

    for line in a.lines() {
        let (first, second) = line.split_once("|").unwrap();
        let (first, second) = (
            first.parse::<usize>().unwrap(),
            second.parse::<usize>().unwrap(),
        );
        rules[first][second] = true;
    }
    let mut s = 0;
    let mut v: Vec<usize> = Vec::with_capacity(100);
    let mut v_s: Vec<usize> = Vec::with_capacity(100);
    for line in b.lines() {
        v.clear();
        v.extend(line.split(",").map(|v| v.parse::<usize>().unwrap()));
        v_s.clear();
        v_s.extend(v.iter());
        v_s.sort_unstable_by(|a, b| match rules[*a][*b] {
            true => std::cmp::Ordering::Less,
            false => std::cmp::Ordering::Greater,
        });
        if v_s == v {
            s += v[v.len() / 2];
        }
    }
    Ok(s as i64)
}

#[cfg(test)]
mod tests {

    #[test]
    fn test_part_5_a() {
        let input = "47|53\n97|13\n97|61\n97|47\n75|29\n61|13\n75|53\n29|13\n97|29\n53|29\n61|53\n97|53\n61|29\n47|13\n75|47\n97|75\n47|61\n75|61\n47|29\n75|13\n53|13\n\n75,47,61,53,29\n97,61,53,29,13\n75,29,13\n75,97,47,61,53\n61,13,29\n97,13,75,29,47";
        assert_eq!(super::part_a(input).unwrap(), 143);
    }
}
