use aoc_in_second::{days::day_1, helpers::inputs::read_input};
use criterion::{black_box, criterion_group, criterion_main, Criterion};

fn criterion_benchmark(c: &mut Criterion) {
    let day_1_input = read_input(1).unwrap();
    c.bench_function("day 1 - part a", |b| {
        b.iter(|| day_1::part_a(black_box(&day_1_input)))
    });
    c.bench_function("day 1 - part b", |b| {
        b.iter(|| day_1::part_b(black_box(&day_1_input)))
    });
}

criterion_group!(benches, criterion_benchmark);
criterion_main!(benches);
