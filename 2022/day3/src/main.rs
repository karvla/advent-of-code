use std::collections::HashSet;

const INPUT: &str = include_str!("../input");

fn priority(c: char) -> u32 {
    if c.is_lowercase() {
        c as u32 - ('a' as u32) + 1
    } else {
        c as u32 - ('A' as u32) + 27
    }
}

fn main() {
    let a: u32 = INPUT
        .lines()
        .map(|l| {
            let len = l.len();
            let (a, b) = l.split_at(len / 2);
            let a_set: HashSet<char> = a.chars().collect();
            let b_set: HashSet<char> = b.chars().collect();
            let mut in_both = a_set.intersection(&b_set);
            return in_both.next().unwrap().clone();
        })
        .map(priority)
        .sum();

    let b: u32 = INPUT
        .lines()
        .collect::<Vec<_>>()
        .chunks(3)
        .map(|group| {
            if let [a, b, c] = group {
                let mut set: HashSet<char> = HashSet::from_iter(a.chars());
                let set_b: HashSet<char> = HashSet::from_iter(b.chars());
                let set_c: HashSet<char> = HashSet::from_iter(c.chars());
                set.retain(|i| set_b.contains(i) && set_c.contains(i));
                return set.iter().next().unwrap().clone();
            }
            return 'c';
        })
        .map(priority)
        .sum();

    println!("Part 1: {}", a);
    println!("Part 2: {}", b);
}
