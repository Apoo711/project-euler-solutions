def solution():
    total_sum = 0
    a, b = 2, 8
    while a <= 4000000:
        total_sum += a
        a, b = b, 4 * b + a
    return total_sum

if __name__ == "__main__":
    print(solution())