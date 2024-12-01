use std::{
    env::join_paths,
    path::{Path, PathBuf},
};

use anyhow::{Error, Result};

pub fn read_input(day: usize) -> Result<String> {
    Ok(std::fs::read_to_string(dbg!(Path::new(env!(
        "CARGO_MANIFEST_DIR"
    ))
    .join(format!("inputs/day_{}.txt", day))))?)
}
