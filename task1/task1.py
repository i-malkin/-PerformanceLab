import sys

def circular_path(n, m):
    array = list(range(1, n + 1))
    path = []
    current_pos = 0

    while len(path) == 0 or path[0] != array[current_pos]:
        path.append(array[current_pos])
        current_pos = (current_pos + m - 1) % n

    print("".join(map(str, path)))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python task1.py n m")
    else:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
        circular_path(n, m)
