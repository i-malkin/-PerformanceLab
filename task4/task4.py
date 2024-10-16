import sys

def read_numbers_from_file(file_path):
    with open(file_path, 'r') as f:
        numbers = [int(line.strip()) for line in f]
    return numbers

def find_median(nums):
    nums.sort()
    n = len(nums)
    if n % 2 == 1:
        return nums[n // 2]
    else:
        return nums[n // 2 - 1]

def calculate_moves(nums, target):
    return sum(abs(num - target) for num in nums)

def main():
    if len(sys.argv) != 2:
        print("Использование: python task4.py <путь_к_файлу>")
        return

    file_path = sys.argv[1]
    nums = read_numbers_from_file(file_path)

    median = find_median(nums)

    moves = calculate_moves(nums, median)

    print(moves)

if __name__ == "__main__":
    main()
