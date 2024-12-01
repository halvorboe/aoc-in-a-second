use std::path::Path;

use anyhow::Result;

pub fn read_input(day: u32) -> Result<String> {
    Ok(std::fs::read_to_string(
        Path::new(env!("CARGO_MANIFEST_DIR")).join(format!("inputs/day_{}.txt", day)),
    )?)
}
