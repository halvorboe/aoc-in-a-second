use aoc_in_a_second::{
    days::{day_1, day_2},
    helpers::inputs::read_input,
};
use criterion::{black_box, criterion_group, criterion_main, Criterion};

fn criterion_benchmark(c: &mut Criterion) {
    let day_1_input = read_input(1).unwrap();
    c.bench_function("day_1_a", |b| {
        b.iter(|| day_1::part_a(black_box(&day_1_input)))
    });
    c.bench_function("day_1_b", |b| {
        b.iter(|| day_1::part_b(black_box(&day_1_input)))
    });
    let day_2_input = read_input(2).unwrap();
    c.bench_function("day_2_a", |b| {
        b.iter(|| day_2::part_a(black_box(&day_2_input)))
    });
    c.bench_function("day_2_b", |b| {
        b.iter(|| day_2::part_b(black_box(&day_2_input)))
    });
}

criterion_group!(benches, criterion_benchmark);
criterion_main!(benches);
