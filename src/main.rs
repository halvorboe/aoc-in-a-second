mod days;
pub mod helpers;

use std::time::Instant;

use anyhow::Result;
use days::day_1;
use helpers::inputs::read_input;

fn main() -> Result<()> {
    let start = Instant::now();
    let input = read_input(1)?;
    assert_eq!(day_1::part_a(&input)?, 1941353);
    assert_eq!(day_1::part_b(&input)?, 22539317);
    println!("Execution time: {:?}", start.elapsed());
    Ok(())
}
