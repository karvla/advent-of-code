const  INPUT: &str = include_str!("../input");

const EX : &str = "A Y
B X
C Z";

type Hand = i32;
type Score = i32;

fn hand(a : &str) -> Hand {
    match a {
        "A" => 1,
        "B" => 2,
        "C" => 3,
        "X" => 1,
        "Y" => 2,
        "Z" => 3,
        _ => -1,
    }
}

fn get_score(a: Hand, b: Hand) -> Score {
    if b > a && !(a == 1 && b == 3) || (a ==3 && b == 1) {
        return 6;
    }
    if a == b {
        return 3;
    }
    return 0;
}

fn get_new_hand(other : Hand, my : Hand) -> Hand {
    match (other, my) {
        (1, 1) => 3,
        (2, 1) => 1,
        (3, 1) => 2,

        (_, 2) => other,

        (1, 3) => 2,
        (2, 3) => 3,
        (3, 3) => 1,

        (_, _) => -100
    }
}

fn main() {
    let a: i32 = INPUT
        .lines()
        .map(|l| {
            let (a, b) = l.split_once(" ").unwrap();
            return get_score(hand(&a), hand(&b)) + hand(&b);
        })
    .sum();

    let b: i32 = INPUT
        .lines()
        .map(|l| {
            let (a, b) = l.split_once(" ").unwrap();
            let new_hand = get_new_hand(hand(&a), hand(&b));
            return get_score(hand(&a), new_hand) + new_hand;
        })
    .sum();

    println!("Part 1: {}", a);
    println!("Part 2: {}", b);

}
