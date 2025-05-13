use regex::Regex;
use std::{fs, time::Instant};

struct Mul {
    a: u64,
    b: u64,
    pos: usize,
}

fn main() {
    let file_name = "src/day03/day03.dat";
    let mut start_time = Instant::now();

    let data = read_data(file_name);
    let result1: u64 = data.iter().fold(0, |agg, mul| agg + mul.a * mul.b);
    println!(
        "Result 1: {result1} {:?}",
        Instant::now().duration_since(start_time)
    );

    start_time = Instant::now();
    let (dos, donts) = read_data_part2(file_name);
    let result2 = data
        .iter()
        .filter(|&mul| {
            let closest_do = get_closest(&dos, mul.pos);
            let closest_dont = get_closest(&donts, mul.pos);
            closest_do >= closest_dont
        })
        .fold(0, |agg, mul| agg + mul.a * mul.b);
    println!(
        "Result 2: {result2} {:?}",
        Instant::now().duration_since(start_time)
    );
}

fn read_data(file_name: &str) -> Vec<Mul> {
    let re = Regex::new(r"mul\((\d+),(\d+)\)").unwrap();

    let raw = fs::read_to_string(file_name).unwrap();
    re.find_iter(raw.as_str())
        .map(|m| {
            let cap = re.captures(m.as_str()).unwrap();
            Mul {
                a: cap[1].parse().unwrap(),
                b: cap[2].parse().unwrap(),
                pos: m.start(),
            }
        })
        .collect()
}

fn read_data_part2(file_name: &str) -> (Vec<usize>, Vec<usize>) {
    let instruct_do = "do()";
    let instruct_dont = "don't()";

    let raw = fs::read_to_string(file_name).unwrap();
    let dos: Vec<_> = raw.match_indices(instruct_do).map(|(i, _)| i).collect();

    let donts: Vec<_> = raw.match_indices(instruct_dont).map(|(i, _)| i).collect();
    return (dos, donts);
}

fn get_closest(indices: &Vec<usize>, index: usize) -> usize {
    indices
        .iter()
        .map(|&i| i)
        .take_while(|&i| i <= index)
        .last()
        .unwrap_or(0)
}
