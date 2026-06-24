def t(a: list[int], b: int) -> list[int]:
    for x in range(len(a)):
        for y in range(x + 1, len(a)):
            if a[x] + a[y] == b:
                return [x, y]
    return []


if __name__ == "__main__":
    print(t([2, 7, 11, 15], 9))  # [0, 1]
    print(t([3, 2, 4], 6))       # [1, 2]
    print(t([3, 3], 6))          # [0, 1]
