def solution():
    total_sum = 0
    a, b = 2, 8
    
    while a <= 4000000:
        total_sum += a
        a, b = b, 4 * b + a
    print(total_sum)

if __name__ == "__main__":
    solution()