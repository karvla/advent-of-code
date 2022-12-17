const INPUT: &str = include_str!("../input");

fn start_end(r: &str) -> (u32, u32) {
    let (s, e) = r.split_once('-').unwrap();
    return (s.parse().unwrap(), e.parse().unwrap());
}

fn main() {
    let a = INPUT
        .lines()
        .filter(|l| {
            let (a, b) = l.split_once(',').unwrap();
            let (sa, ea) = start_end(a);
            let (sb, eb) = start_end(b);

            return sa <= sb && ea >= eb || sb <= sa && eb >= ea;
        })
        .count();

    let b = INPUT
        .lines()
        .filter(|l| {
            let (a, b) = l.split_once(',').unwrap();
            let (sa, ea) = start_end(a);
            let (sb, eb) = start_end(b);

            return ea >= sb && sa <= eb;
        })
        .count();

    println!("Part 1: {}", a);
    println!("Part 2: {}", b);
}
