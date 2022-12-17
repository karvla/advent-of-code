const INPUT: &str = include_str!("../input");


fn main() {
    let mut u: Vec<i32> = INPUT
        .split("\n\n")
        .map(|g| {
            g
                .lines()
                .map(|i| i.parse::<i32>().unwrap())
                .sum::<i32>()
        
        })
        .collect();

    u.sort();
    u.reverse();
    println!("Part 1: {}", u[0]);
    println!("Part 2: {}", u[0..3].iter().sum::<i32>());

}
