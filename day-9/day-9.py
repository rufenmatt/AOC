from dataclasses import dataclass

with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

@dataclass
class Point:
    x: int
    y: int

    def add(self, dx: int, dy: int) -> "Point":
        return Point(self.x + dx, self.y + dy)

    def distance(self, other: "Point") -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __hash__(self) -> int:
        return hash((self.x, self.y))

def part1(lines):
    head = Point(0, 0)
    tail = Point(0, 0)

    seen = set()

    for motions in lines:
        direction, steps = motions.split(" ")

        for _ in range(int(steps)):
            dx, dy = {
                "U": (0, -1),
                "D": (0, 1),
                "L": (-1, 0),
                "R": (1, 0)
            }[direction]

            head = head.add(dx, dy)

            if (head.x == tail.x and abs(head.y - tail.y) == 2) or (head.y == tail.y and abs(head.x - tail.x) == 2):
                tail = tail.add(dx, dy)
            elif head.distance(tail) == 3:
                dirs = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
                tail = min([tail.add(dx, dy) for dx, dy in dirs], key=lambda point: head.distance(point))

            seen.add(tail)
    return len(seen)

def part2(lines):
    head = Point(0, 0)
    tails = [Point(0, 0) for _ in range(9)]

    seen = set()

    for motions in lines:
        direction, steps = motions.split(" ")
        for _ in range(int(steps)):
                    dx, dy = {
                        "U": (0, -1),
                        "D": (0, 1),
                        "L": (-1, 0),
                        "R": (1, 0)
                    }[direction]

                    head = head.add(dx, dy)

                    for i in range(9):
                        nxt = head if i == 0 else tails[i - 1]
                        tail = tails[i]

                        if (nxt.x == tail.x and abs(nxt.y - tail.y) == 2) or (nxt.y == tail.y and abs(nxt.x - tail.x) == 2):
                            dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
                        elif nxt.distance(tail) >= 3:
                            dirs = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
                        else:
                            continue

                        tails[i] = min([tail.add(dx, dy) for dx, dy in dirs], key=lambda point: nxt.distance(point))

                    seen.add(tails[-1])

    return len(seen)

if __name__ == "__main__":
    print('Part 1 solution:', part1(lines))
    print('Part 2 solution:', part2(lines))
