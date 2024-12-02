mod days;
pub mod helpers;

use std::time::Instant;

use anyhow::Result;
use clap::command;
use clap::Parser;
use days::day_1;
use days::day_2;
use days::day_3;
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
        for day in 1..=3 {
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
            assert_eq!(day_3::part_a(&input)?, 0);
            assert_eq!(day_3::part_b(&input)?, 0);
        }
        _ => println!("Day {} is not implemented yet.", day),
    }
    println!("Execution time for day {}: {:?}", day, day_start.elapsed());
    Ok(())
}
