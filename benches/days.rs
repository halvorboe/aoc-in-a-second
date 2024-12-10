use aoc_in_a_second::{days::*, helpers::inputs::read_input};
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
    let day_3_input = read_input(3).unwrap();
    c.bench_function("day_3_a", |b| {
        b.iter(|| day_3::part_a(black_box(&day_3_input)))
    });
    c.bench_function("day_3_b", |b| {
        b.iter(|| day_3::part_b(black_box(&day_3_input)))
    });
    let day_4_input = read_input(4).unwrap();
    c.bench_function("day_4_a", |b| {
        b.iter(|| day_4::part_a(black_box(&day_4_input)))
    });
    c.bench_function("day_4_b", |b| {
        b.iter(|| day_4::part_b(black_box(&day_4_input)))
    });
    let day_5_input = read_input(5).unwrap();
    c.bench_function("day_5_a", |b| {
        b.iter(|| day_5::part_a(black_box(&day_5_input)))
    });
    c.bench_function("day_5_b", |b| {
        b.iter(|| day_5::part_b(black_box(&day_5_input)))
    });
    let day_6_input = read_input(6).unwrap();
    c.bench_function("day_6_a", |b| {
        b.iter(|| day_6::part_a(black_box(&day_6_input)))
    });
    c.bench_function("day_6_b", |b| {
        b.iter(|| day_6::part_b(black_box(&day_6_input)))
    });
    let day_7_input = read_input(7).unwrap();
    c.bench_function("day_7_a", |b| {
        b.iter(|| day_7::part_a(black_box(&day_7_input)))
    });
    c.bench_function("day_7_b", |b| {
        b.iter(|| day_7::part_b(black_box(&day_7_input)))
    });
}

criterion_group!(benches, criterion_benchmark);
criterion_main!(benches);
