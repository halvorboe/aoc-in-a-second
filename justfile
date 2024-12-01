day day_number:
    cargo run --release  -- --day {{day_number}}

all:
    cargo run --release -- --all-days

bench day_number:
    cargo bench -- day_{{day_number}}_*

benchall:
    cargo bench

benchreport:
    open target/criterion/report/index.html