use std::{fs, time::Instant};

fn main() {
    let data = read_data("src/day02/day02.dat");

    let start_time1 = Instant::now();
    let result1 = data
        .iter()
        .filter(|&row| is_increasing(row) || is_decreasing(row))
        .count();
    println!("Result 1: {result1} {:?}", Instant::now().duration_since(start_time1));

    let start_time2 = Instant::now();
    let result2 = data.into_iter().filter(test_all).count();
    println!("Result 2: {result2} {:?}", Instant::now().duration_since(start_time2))
}

fn is_increasing(input: &Vec<u64>) -> bool {
    input
        .into_iter()
        .zip(input.into_iter().skip(1))
        .all(|(&a, &b)| {
            return a < b && (b - a) <= 3;
        })
}

fn is_decreasing(input: &Vec<u64>) -> bool {
    let mut new_input = input.clone();
    new_input.reverse();
    is_increasing(&new_input)
}

fn test_all(input: &Vec<u64>) -> bool {
    if is_increasing(input) || is_decreasing(input) {
        return true;
    }
    return input.iter().enumerate().any(|(i, _)| {
        let mut test_vec: Vec<u64> = Vec::new();
        for (x, &val) in input.iter().enumerate() {
            if x != i {
                test_vec.push(val);
            }
        }
        return is_increasing(&test_vec) || is_decreasing(&test_vec);
    });
}

fn read_data(file_name: &str) -> Vec<Vec<u64>> {
    fs::read_to_string(file_name)
        .unwrap()
        .split("\n")
        .map(|line| {
            line.split(" ")
                .map(|val| val.parse::<u64>().unwrap())
                .collect::<Vec<u64>>()
        })
        .collect()
}
