use std::{fs, time::Instant};

fn main() {
    let data = read_data("src/day01/day01.dat");
    let (sorted, s_left, s_right) = match_sorted(data);
    let mut start_time = Instant::now();
    let result1 = sorted
        .iter()
        .map(|(left, right)| {
            if left > right {
                left - right
            } else {
                right - left
            }
        })
        .fold(0, |x, n| x + n);
    println!("Result 1: {result1} {:?}", Instant::now().duration_since(start_time));

    start_time = Instant::now();
    let result2: u64 = s_left.iter().fold(0, |acc, num| {
        let count: u64 = s_right.clone().into_iter().filter(|c| *c == *num).count() as u64;
        acc + num * count
    });
    println!("Result 1: {result2} {:?}", Instant::now().duration_since(start_time))
}

fn match_sorted(input: Vec<(u64, u64)>) -> (Vec<(u64, u64)>, Vec<u64>, Vec<u64>) {
    let mut list1: Vec<u64> = Vec::new();
    let mut list2: Vec<u64> = Vec::new();
    input.iter().for_each(|(a, b)| {
        list1.push(*a);
        list2.push(*b);
    });
    list1.sort();
    list2.sort();
    return (
        list1.clone().into_iter().zip(list2.clone()).collect(),
        list1,
        list2,
    );
}

fn read_data(file_name: &str) -> Vec<(u64, u64)> {
    fs::read_to_string(file_name)
        .unwrap()
        .split("\n")
        .map(|line| {
            line.split("   ")
                .map(|x| x.parse::<u64>().unwrap())
                .collect::<Vec<u64>>()
        })
        .map(|v| (*v.first().unwrap(), *v.get(1).unwrap()))
        .collect()
}
