use std::collections::HashSet;

const INPUT: &str = include_str!("../input");

fn get_start_message(window_size: usize) -> Option<usize> {
    let char_index = INPUT.chars().enumerate().collect::<Vec<(usize, char)>>();

    let window = char_index.windows(window_size).find(|window| {
        return window_size == HashSet::<&char>::from_iter(window.iter().map(|(_, c)| c)).len();
    });

    match window {
        Some(w) => return Some(w.last().unwrap().0 + 1),
        None => return None,
    }
}

fn main() {
    match get_start_message(4) {
        Some(v) => println!("Part 1: {}", v),
        None => {}
    }
    match get_start_message(14) {
        Some(v) => println!("Part 2: {}", v),
        None => {}
    }
}
