use std::collections::LinkedList;

const INPUT: &str = include_str!("../input");

fn get_moves() -> impl Iterator<Item = [usize; 3]> {
    return INPUT.lines().filter_map(|line| {
        if let [n, from, to] = Vec::<usize>::from_iter(
            line.split_whitespace()
                .filter_map(|string| string.parse().ok()),
        )[..]
        {
            return Some([n, from, to]);
        }
        return None;
    });
}

type Stack = Vec<LinkedList<char>>;

fn get_stacks() -> Stack {
    let mut stacks = vec![LinkedList::<char>::new(); 10];

    // Parse initial stacks
    for line in INPUT.lines().collect::<Vec<&str>>()[..8].iter() {
        for (i, c) in line.chars().enumerate() {
            if (i + 3) % 4 == 0 && c != ' ' {
                stacks[i / 4 + 1].push_front(c);
            }
        }
    }
    return stacks;
}

fn main() {
    // Part 1
    let mut stacks_1 = get_stacks();
    for [n, from, to] in get_moves() {
        for _ in 0..n {
            match stacks_1[from].pop_back() {
                Some(v) => stacks_1[to].push_back(v),
                None => println!("No values in stack {}", from),
            };
        }
    }
    println!(
        "Part 1: {}",
        stacks_1.iter().filter_map(|s| s.back()).collect::<String>()
    );

    // Part 2
    let mut stacks_2 = get_stacks();
    for [n, from, to] in get_moves() {
        let mut temp = LinkedList::<char>::new();
        for _ in 0..n {
            match stacks_2[from].pop_back() {
                Some(v) => temp.push_front(v),
                None => println!("No values in stack {}", from),
            };
        }
        stacks_2[to].extend(temp);
    }
    println!(
        "Part 2: {}",
        stacks_2.iter().filter_map(|s| s.back()).collect::<String>()
    );
}
