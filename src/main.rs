mod days;
pub mod helpers;

use std::time::Instant;

use anyhow::Result;
use clap::command;
use clap::Parser;
use days::*;
use helpers::inputs::read_input;

#[derive(Parser)]
#[command(author, version, about)]
struct Cli {
    #[arg(short, long)]
    day: Option<u32>,

    #[arg(long)]
    all_days: bool,
}

fn main() -> Result<()> {
    let args = Cli::parse();

    let start = Instant::now();

    if args.all_days {
        for day in 1..=7 {
            run_day(day)?;
        }
    } else if let Some(day) = args.day {
        run_day(day)?;
    } else {
        panic!("Please specify a day using --day <day> or use --all-days to run all.");
    }

    println!("Total execution time: {:?}", start.elapsed());
    Ok(())
}

fn run_day(day: u32) -> Result<()> {
    let input = read_input(day)?;
    let day_start = Instant::now();
    match day {
        1 => {
            assert_eq!(day_1::part_a(&input)?, 1941353);
            assert_eq!(day_1::part_b(&input)?, 22539317);
        }
        2 => {
            assert_eq!(day_2::part_a(&input)?, 472);
            assert_eq!(day_2::part_b(&input)?, 520);
        }
        3 => {
            assert_eq!(day_3::part_a(&input)?, 178538786);
            assert_eq!(day_3::part_b(&input)?, 102467299);
        }
        4 => {
            assert_eq!(day_4::part_a(&input)?, 2578);
            assert_eq!(day_4::part_b(&input)?, 1972);
        }
        5 => {
            assert_eq!(day_5::part_a(&input)?, 6612);
            assert_eq!(day_5::part_b(&input)?, 4944);
        }
        6 => {
            assert_eq!(day_6::part_a(&input)?, 5242);
            // wrong answer currently
            assert_eq!(day_6::part_b(&input)?, 1577); // 1424);
        }
        7 => {
            assert_eq!(day_7::part_a(&input)?, 0);
            assert_eq!(day_7::part_b(&input)?, 0);
        }
        _ => println!("Day {} is not implemented yet.", day),
    }
    println!("Execution time for day {}: {:?}", day, day_start.elapsed());
    Ok(())
}
