const INPUT: &str = include_str!("../input");

fn is_visible(y: usize, x: usize, forest: &Vec<Vec<usize>>) -> bool {
    let tree_height = forest[y][x];
    let row = &forest[y];
    let column = forest.iter().map(|row| row[x]).collect::<Vec<usize>>();

    let (h, w) = (forest.len(), forest[0].len());

    return (0..x).map(|x| row[x]).all(|h| h < tree_height)
        || ((x + 1)..w).map(|x| row[x]).all(|h| h < tree_height)
        || (0..y).map(|y| column[y]).all(|h| h < tree_height)
        || ((y + 1)..h).map(|y| column[y]).all(|h| h < tree_height);
}

fn score(y: usize, x: usize, forest: &Vec<Vec<usize>>) -> usize {
    let tree_height = forest[y][x];
    let row = &forest[y];
    let column = forest.iter().map(|row| row[x]).collect::<Vec<usize>>();

    let (h, w) = (forest.len(), forest[0].len());

    let directions: Vec<Vec<usize>> = vec![
        (0..y).rev().map(|i| column[i]).collect(),
        (0..x).rev().map(|i| row[i]).collect(),
        (y..h).skip(1).map(|i| column[i]).collect(),
        (x..w).skip(1).map(|i| row[i]).collect(),
    ];

    let mut scores: Vec<usize> = vec![];
    for dir in &directions {
        let mut i = 0;
        for h in dir {
            i += 1;
            if h >= &tree_height {
                break;
            }
        }
        scores.push(i);
    }

    return scores.into_iter().reduce(|a, b| a * b).unwrap_or(0);
}

fn main() {
    println!("{:?}", (4..0).collect::<Vec<usize>>());
    let width = INPUT.lines().collect::<Vec<&str>>().len();
    let height = INPUT.lines().next().unwrap().len();
    let mut forest = vec![vec![0 as usize; width]; height];
    for (y, line) in INPUT.lines().enumerate() {
        for (x, tree_height) in line.char_indices() {
            forest[y][x] = tree_height.to_digit(10).unwrap_or(0) as usize;
        }
    }
    let n_visible = (0..height)
        .map(|y| (0..width).map(move |x| (y, x)))
        .flatten()
        .filter(|(y, x)| is_visible(*y, *x, &forest))
        .count();

    println!("Part 1: {}", n_visible);

    let max_score = (0..height)
        .map(|y| (0..width).map(move |x| (y, x)))
        .flatten()
        .map(|(y, x)| score(y, x, &forest))
        .max()
        .unwrap_or(0);
    println!("Part 2: {}", max_score);
}
