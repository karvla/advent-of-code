use std::collections::HashMap;

const INPUT: &str = include_str!("../input");

fn main() {
    let mut paths = HashMap::<String, i32>::new();
    let mut parents = Vec::<String>::new();

    for line in INPUT.lines() {
        let parts: Vec<_> = line.split_whitespace().collect();
        match parts[..] {
            ["$", "cd", ".."] => {
                parents.pop();
            }
            ["$", "cd", dir] => {
                parents.push(format!(
                    "{}/{}",
                    parents.last().unwrap_or(&String::from("")),
                    dir
                ));
            }
            ["$", "ls"] => continue,
            ["dir", _] => continue,
            [size, _] => {
                let size: i32 = size.parse().expect("could not parse file size");
                parents.iter().for_each(|p| {
                    match paths.get(p) {
                        Some(v) => paths.insert(p.to_string(), v + size),
                        None => paths.insert(p.to_string(), size),
                    };
                });
            }
            _ => {}
        };
    }

    println!(
        "Part 1: {}",
        paths
            .clone()
            .into_values()
            .filter(|v| *v <= 100_000)
            .sum::<i32>()
    );

    let min_size = 30_000_000 - 70_000_000 + paths.get("//").unwrap_or(&0);
    println!(
        "Part 2: {}",
        paths
            .into_values()
            .filter(|v| *v >= min_size)
            .min()
            .unwrap_or(0)
    );
}
