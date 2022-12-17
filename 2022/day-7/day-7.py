from pathlib import Path
from collections import defaultdict

with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

def get_dir_sizes(lines):
    current_dir = Path("/")
    dir_sizes = defaultdict(int)

    for line in lines:
        if line.startswith("$ cd"):
            current_dir = (current_dir / line[5:]).resolve()
        elif line.startswith("$ ls"):
            continue
        elif line.startswith("dir"):
            continue
        else:
            size = int(line.split(" ")[0])
            dir_sizes[current_dir] += size
            for parent in current_dir.parents:
                dir_sizes[parent] += size
    return dir_sizes

def part1(lines):
    dir_sizes = get_dir_sizes(lines)

    return sum(v for v in dir_sizes.values() if v <= 100000)

def part2(lines):
    dir_sizes = get_dir_sizes(lines)
    unused_space = dir_sizes[Path("/")]
    required = 30000000 - (70000000 - unused_space)

    return min(v for v in dir_sizes.values() if v >= required)

if __name__ == "__main__":
    print('Part 1 solution:', part1(lines))
    print('Part 2 solution:', part2(lines))
